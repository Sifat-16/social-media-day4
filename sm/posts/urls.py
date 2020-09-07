from django.urls import path
from .views import *

urlpatterns = [
    path('', newsfeed, name="newsfeed"),
    path('post/update/<int:id>', updatepost, name="update-post"),
    path('post/delete/<int:id>', deletepost, name="delete-post"),
    path('comment/update/<int:id>', updatecomment, name="update-comment"),
    path('comment/delete/<int:id>', deletecomment, name="delete-comment"),
    path('detail/<int:id>', detailpost, name="detail"),
    path('submit-comment', subcom, name="comment"),
    path('submit-post', subpost, name="subpost"),
    path('like', like, name="like-post"),
    path('unlike', unlike, name="unlike-post"),

]

