from tkinter import FLAT
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from facebook.models import Profile,Post,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse



@login_required(login_url='login')
def home(request):
    profile = Profile.objects.all()
    post = Post.objects.all().order_by('-created')
    comments = Comment.objects.all()
    return render(request,'facebook/home.html',{"post":post,'comments':comments,'profile':profile})

def login_user(request):
    error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            error = "Username Not Found"
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            error = "Username or password incorrect"
    
    return render(request,'facebook/login.html',{"error":error})
  
def signup_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            try:
                user = authenticate(username=username,password=password)
                Profile.objects.create(
                    user=user,
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    imageUrl=request.POST['imageUrl'],
                    city=request.POST['city'],
                    date=request.POST['date'],
                )
                login(request,user)
                return redirect('home')
            except:
                return render(request,'facebook/signup.html',{"error":"error creating the user"})
    return render(request,'facebook/signup.html',dict({"form":form}))

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request,username):
    post = Post.objects.filter(user__username=username).order_by('-created')
    profile = Profile.objects.filter(user__username=username)
    comments = Comment.objects.all()
    return render(request,'facebook/profile.html',{'profile':profile,'post':post,'comments':comments})

@login_required(login_url='login')
def add_friend(request,username1):

    self_profile = User.objects.get(username=request.user)
    self_profile1 = Profile.objects.get(user=self_profile)
    friend_profile = User.objects.get(username=username1)
    friend_profile1 = Profile.objects.get(user=friend_profile)

    if request.method == 'POST' :
        if friend_profile1 not in self_profile1.friends.all():
            self_profile1.friends.add(friend_profile1.id)
            return redirect('profile',username1)

        else:
            self_profile1.friends.remove(friend_profile1.id)
            return redirect('profile', username1)




@login_required(login_url='login')
def edit_profile(request,username):
    edit = Profile.objects.get(user__username=username)
    if edit.user == request.user.profile.user:
        if request.method == 'POST':
            edit.imageUrl=request.POST['imageUrl']
            edit.last_name=request.POST['lastname']
            edit.first_name=request.POST['firstname']
            edit.date=request.POST['date']
            edit.city=request.POST['adress']
            edit.save()
            return redirect('profile',username)
        return render(request,'facebook/editprofile.html',{"edit":edit})
    else:
        return redirect('home')


def profile_about(request,username):
    about = Profile.objects.filter(user__username=username)
    return render(request,'facebook/profileabout.html',{"about":about})

def profile_friends(request,username):
    friend = list(Profile.objects.filter(user__username=username))
    return render(request,'facebook/profilefriends.html',{"friend":friend})


def profile_remove(request,username):
    profile = User.objects.filter(username=username)
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    return render(request,'facebook/profileremove.html',{'profile':profile})

@login_required(login_url='login')
def addpost(request,id):
    profile = id
    if request.method == 'POST':
        Post.objects.create(
            body=request.POST['body'],
            imageUrl=request.POST['imageUrl'],
            user=request.user,
        )
        return redirect('home')
    return render(request,'facebook/newpost.html',{"profile":profile})


@login_required(login_url='login')
def post(request,id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)
    return render(request,'facebook/post.html',{"post":post,"comments":comments})

def addlike(request,id):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.profile.id).exists():
        post.likes.remove(request.user.profile.id)
        print()
    else:
        post.likes.add(request.user.profile.id)
    return HttpResponseRedirect(reverse('post', args=[str(id)]))

@login_required(login_url='login')
def addcomment(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        Comment.objects.create(
            body=request.POST['body'],
            post=post,
            user=request.user
        )
        return redirect('post',post.id)


@login_required(login_url='login')
def edit_post(request,id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        if request.method == 'POST':
            post.imageUrl=request.POST['imageUrl']
            post.body=request.POST['body']
            post.save()
            return redirect('post',post.id)
        return render(request,'facebook/editpost.html',{"post":post})
    else:
        return redirect('home')
    

@login_required(login_url='login')
def remove_post(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request,'facebook/removepost.html',{'post':post})

@login_required(login_url='login')
def remove_comment(request,id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        comment.delete()
        return redirect('post',comment.post.id)
    return render(request,'facebook/removecomment.html',{'comment':comment})
    

@login_required(login_url='login')
def edit_comment(request,id):
    comment = Comment.objects.get(id=id)
    if comment.user == request.user:
        if request.method == 'POST':
            comment.body=request.POST['body']
            comment.save()
            return redirect('post',comment.post.id)
        return render(request,'facebook/editcomment.html',{"comment":comment})
    else:
        return redirect('home')

# @login_required(login_url='login')
# def group(request):
#     return render(request,'facebook/group.html',{})

# @login_required(login_url='login')
# def new_group(request):
#     return render(request,'facebook/newgroup.html',{})

# @login_required(login_url='login')
# def edit_group(request):
#     return render(request,'facebook/editgroup.html',{})

# @login_required(login_url='login')
# def remove_group(request):
#     return render(request,'facebook/removegroup.html',{})

def search(request):
    q = request.GET.get('q')
    results = Post.objects.filter(
        Q(body__icontains=q) 
    )
    q = request.GET.get('q')
    profiles = Profile.objects.filter(
        Q(first_name__icontains=q) |
        Q(last_name__icontains=q) 
    )
    return render(request,'facebook/search.html',{"results":results,'profiles':profiles})

