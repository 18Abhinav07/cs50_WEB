from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
from django.core.paginator import Paginator



def index(request):
    if request.method == "POST":
        content = request.POST["content"]
        user = request.user
        new_post = Post(user=user, content=content)
        new_post.save()
        print(new_post.content)

    all_posts = Post.objects.all().order_by('-id')  # Order by the newest post

    # Pagination
    paginator = Paginator(all_posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    likes = []
    dislikes = []

    for post in page_obj:
        likes.append(post.likes.count())
        dislikes.append(post.dislikes.count())

    values = list(zip(page_obj, likes, dislikes))

    return render(request, "network/index.html", {"values": values, "page_obj": page_obj})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

@login_required
def following(request):
    user = request.user
    following_users = [u for u in User.objects.all() if user in u.followers.all()]
    following_posts = Post.objects.filter(user__in=following_users).order_by('-id')

    # Pagination
    paginator = Paginator(following_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    likes = []
    dislikes = []

    for post in page_obj:
        likes.append(post.likes.count())
        dislikes.append(post.dislikes.count())

    values = list(zip(page_obj, likes, dislikes))

    return render(request, "network/following.html", {"values": values, "page_obj": page_obj})


def user_info(request, pk):
    post = Post.objects.get(id=pk)
    post_user = User.objects.get(pk=post.user.id)
    all_posts = Post.objects.filter(user=post_user.id).order_by('-id')

    is_following = post_user.followers.filter(pk=request.user.id).exists()

    # Pagination
    paginator = Paginator(all_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    likes = []
    dislikes = []
    is_liking = []
    is_disliking = []

    for post in page_obj:
        likes.append(post.likes.count())
        dislikes.append(post.dislikes.count())
        is_liking.append(post.likes.filter(pk=request.user.id).exists())
        is_disliking.append(post.dislikes.filter(pk=request.user.id).exists())

    values = list(zip(page_obj, likes, dislikes, is_liking,is_disliking))

    return render(request, "network/user_info.html", {
        "values": values,
        "follower_count": post_user.count_followers(),
        "following_count": post_user.count_following(),
        "post_user": post_user,
        "is_following": is_following,
        "page_obj": page_obj
    })
    
    
def like(request,pk):
    post = Post.objects.get(id = pk)
    if post.dislikes.filter(pk = request.user.id).exists():
        post.dislikes.remove(request.user)
    post.likes.add(request.user)
    post.save()
    likes = post.likes.count()
    dislikes = post.dislikes.count()
    return JsonResponse({"likes":likes,"dislikes":dislikes})
     
    
def dislike(request,pk):
    post = Post.objects.get(id = pk)
    if post.likes.filter(pk = request.user.id).exists():
        post.likes.remove(request.user)
    post.dislikes.add(request.user)
    post.save()
    likes = post.likes.count()
    dislikes = post.dislikes.count()
    return JsonResponse({"likes":likes,"dislikes":dislikes})
    

def follow(request,pk):
    user = User.objects.get(id = pk)
    user.followers.add(request.user)
    user.save()
    counts = user.followers.count()
    return JsonResponse({"followers":counts})
    
    
def unfollow(request,pk):
    user = User.objects.get(id = pk)
    user.followers.remove(request.user)
    user.save()
    counts = user.followers.count()
    return JsonResponse({"followers":counts})
    
    
@login_required
def update_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found or unauthorized.'}, status=404)

    if request.method == 'POST':
        data = json.loads(request.body)
        new_content = data.get('content')
        if new_content:
            post.content = new_content
            post.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'No new content provided.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400) 