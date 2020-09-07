from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.template.defaultfilters import slugify
from .code import generate_code


# Create your models here.

INTEREST = (
    ('Male', 'Male'),
    ('Female', 'Female')
)


class Profile(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile/', default='avatar.png',
                                    validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    cover_pic = models.ImageField(upload_to='cover/', default='avatar.png',
                                    validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    email = models.EmailField(max_length=200, default="admin@mail.com")

    profession = models.CharField(max_length=250, default="No profession Added")
    interest = models.CharField(max_length=6, choices=INTEREST, default="Male & Female")

    bio = models.TextField(default="No bio Added")
    country = models.CharField(max_length=100, blank=True)

    friends = models.ManyToManyField(User, related_name='friend')

    language = models.CharField(max_length=100, default='English')

    slug = models.SlugField(unique=True, blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    @property
    def profileURL(self):
        try:
            url = self.profile_pic.url

        except:
            url = ''

        return url

    @property
    def coverURL(self):
        try:
            url = self.cover_pic.url

        except:
            url = ''

        return url

    def save(self, *args, **kwargs):
        exist = False

        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name) + '' + str(self.last_name))
            exist = Profile.objects.filter(slug=to_slug)

            while exist:
                to_slug = slugify(str(to_slug) + '' + str(generate_code))
                exist = Profile.objects.filter(slug=to_slug)

        else:
            to_slug = slugify(str(self.user))

        self.slug = to_slug
        super().save(*args, **kwargs)


    def __str__(self):
        return str(self.user)

        


STATUS = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

BLOCK = (
    ('block', 'block'),
    ('unblock', 'unblock')
)

    
class Relation(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS, null=True)
    block = models.CharField(max_length=7, choices=BLOCK, default='unblock', null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.receiver} {self.status} and {self.block}"
