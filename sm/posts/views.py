from django.shortcuts import render, redirect
from .forms import *
from profiles.models import Profile


# Create your views here.


def newsfeed(request):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    friends = myprofile.friends.all()
    post = Post.objects.all().order_by('-id')
    post_f = PostForm()
    comment_f = CommentForm()
    notification = Notification.objects.filter(
        not_receiver=myprofile).order_by('-id')
    total_notification = Notification.objects.filter(
        not_receiver=myprofile).count()


    

    context = {'pf': post_f, 'post': post, 'cf': comment_f,
               'myprofile': myprofile, 'nt': notification, 'tn': total_notification, 'friends': friends}

    return render(request, 'posts/newsfeed.html', context)

#submitpost
def subpost(request):
    post_f = PostForm()
    me = request.user
    myprofile = Profile.objects.get(user=me)

    if 'submit_post' in request.POST:
        post_f = PostForm(request.POST, request.FILES)
        if post_f.is_valid():
            instance = post_f.save(commit=False)

            instance.author = myprofile
            instance.save()
            post_f = PostForm()
            return redirect('newsfeed')
    return redirect('newsfeed')


#submitcomment
def subcom(request):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    comment_f = CommentForm()
    if 'submit_comment' in request.POST:
        comment_f = CommentForm(request.POST)
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if comment_f.is_valid():
            instance = comment_f.save(commit=False)
            instance.user = myprofile
            instance.post = post_obj
            instance.save()
            if myprofile != post_obj.author:
                Notification.objects.create(
                    not_sender=myprofile, not_receiver=post_obj.author, post=post_obj, status='commented')
            comment_f = CommentForm()
            return redirect('newsfeed')
    return redirect('newsfeed')

#updatepost
def updatepost(request, id):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    post_obj = Post.objects.get(id=id)
    post_f = PostForm(request.POST or None,
                      request.FILES or None, instance=post_obj)

    if request.method == 'POST':

        if post_f.is_valid():
            post_f.save()
            return redirect('newsfeed')

    context = {'pf': post_f, 'mp': myprofile, 'pb': post_obj}
    return render(request, 'posts/updatepost.html', context)


def deletepost(request, id):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    post_obj = Post.objects.get(id=id)

    if request.method == 'POST':
        post_obj.delete()
        return redirect('newsfeed')
    context = {'pb': post_obj}
    return render(request, 'posts/deletepost.html', context)


def updatecomment(request, id):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    comment_obj = Comment.objects.get(id=id)
    comment_f = CommentForm(request.POST or None, instance=comment_obj)

    if request.method == 'POST':

        if comment_f.is_valid():
            comment_f.save()
            return redirect('newsfeed')

    context = {'cf': comment_f, 'mp': myprofile, 'cb': comment_obj}
    return render(request, 'posts/updatecomment.html', context)


def deletecomment(request, id):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    comment_obj = Comment.objects.get(id=id)

    if request.method == 'POST':
        comment_obj.delete()

        return redirect('newsfeed')
    context = {'cb': comment_obj}
    return render(request, 'posts/deletecomment.html', context)


def detailpost(request, id):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    detail_post = Post.objects.get(id=id)
    comment_f = CommentForm()

    context = {'myprofile': myprofile, 'dp': detail_post, 'cf': comment_f}

    return render(request, 'posts/detail.html', context)

#like
def like(request):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    if 'like' in request.POST:
        post_id = request.POST.get('like_id')
        post_obj = Post.objects.get(id=post_id)

        post_obj.liked.add(myprofile)

        post_obj.save
        if myprofile != post_obj.author:

            Notification.objects.create(
                not_sender=myprofile, not_receiver=post_obj.author, post=post_obj, status='liked')

        return redirect('newsfeed')
    return redirect('newsfeed')


#unlike
def unlike(request):
    me = request.user
    myprofile = Profile.objects.get(user=me)
    if 'unlike' in request.POST:
        post_id = request.POST.get('unlike_id')
        post_obj = Post.objects.get(id=post_id)

        post_obj.liked.remove(myprofile)

        post_obj.save
        if myprofile != post_obj.author:
                nots = Notification.objects.get(
                    not_sender=myprofile, not_receiver=post_obj.author, post=post_obj, status='liked')
                nots.delete()


                return redirect('newsfeed')
    return redirect('newsfeed')
