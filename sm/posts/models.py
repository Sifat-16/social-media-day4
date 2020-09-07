from django.db import models
from django.core.validators import FileExtensionValidator
from profiles.models import Profile

COMMENT = (
    ('allow-comment', 'allow-comment'),
    ('not-allow-comment', 'not-allow-comment')
)

POSTS = (
    ('public', 'public'),
    ('friends', 'friends')
)

# Create your models here.
class Post(models.Model):
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', blank=True, validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author')
    liked = models.ManyToManyField(Profile, related_name='likes')
    comment_choice = models.CharField(
        max_length=17, choices=COMMENT, default='allow-comment')
    visibility = models.CharField(max_length=7, choices=POSTS, default='public')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url

    def num_of_likes(self):
        return self.liked.all().count()

    def num_of_comments(self):
        return self.comment_set.all().count()


    def __str__(self):
        return str(self.content[:10])

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body[:10])

LIKE = (
    ('like', 'like'),
    ('unlike', 'unlike')
)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=6, choices=LIKE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


NOTI = (
    ('liked', 'liked'),
    ('commented', 'commented'),
    ('friend', 'friend'),
    ('accept', 'accept')
)

class Notification(models.Model):
    not_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='not_sender')
    not_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='not_receiver')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    status = models.CharField(max_length=9, choices=NOTI, default='liked')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.not_sender} to {self.not_receiver} liked"
