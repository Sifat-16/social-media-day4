from django import forms
from .models import *


COMMENT = (
    ('allow-comment', 'allow-comment'),
    ('not-allow-comment', 'not-allow-comment')
)

POSTS = (
    ('public', 'public'),
    ('friends', 'friends')
)

class PostForm(forms.ModelForm):
    visibility = forms.ChoiceField(
        widget=forms.RadioSelect, choices=POSTS)
    comment_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=COMMENT)
    class Meta:
        
        model = Post
        fields = ['content', 'image', 'comment_choice', 'visibility']

        widgets = {
            'content': forms.Textarea(attrs={'rows': '2', 'placeholder': 'write something'}),
            'comment_choice': forms.TextInput(attrs={'type': 'radio', 'checked': 'checked', 'name': 'radio'}),
            'visibility': forms.TextInput(attrs={'type': 'radio', 'checked': 'checked', 'name': 'radio'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Post your comment'})
        }
