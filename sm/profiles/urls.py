from django.urls import path
from .views import *

urlpatterns = [
    path('myprofile', mytimeline, name="my-time-line"),
    path('myabout', myabout, name="about"),
    path('update', updateprofile, name="myupdate"),
    path('lists', friends, name="peoples"),
    path('sendrequest', sendrequest, name="send-request"),
    path('acceptrequest', acceptrequest, name="accept-request"),
    path('removefriend', removefriend, name="remove-friend"),
    path('cancelrequest', cancelrequest, name="cancel-request"),
    path('ignorerequest', ignorerequest, name="ignore-request"),
    path('block', blockfriend, name="block-friend"),
    path('unblock', unblock, name="ub")


]
