from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from accounts.forms import *
from django.contrib.auth.decorators import login_required







def home(request):
    if not request.user.is_authenticated:
         return render(request, 'accounts/login.html')
    else:
        posts=Blog.objects.filter(user=request.user)
    fields=CategoryTree.objects.all()
    if request.user.is_authenticated:
        info=Individual_info()
        info=Individual_info.objects.filter(user=request.user)
        return render(request, 'artistapp/index.html',{'fields':fields,'posts':posts,'info':info})
    else:
        return render(request, 'artistapp/index.html',{'fields':fields,'posts':posts,})

def mypage(request):
     #블로그 글들을 모조리 띄워주는 코드
    #posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'artistapp/mypage.html', {'posts':posts})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베이스로부터 갖고 와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail. html로 띄우는 코드

    comment_form = CommentForm()

    return render(request, 'artistapp/detail.html', {'blog_detail':blog_detail,'comment_form':comment_form})

def create_comment(request, blog_id): 
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        #입력을 받을 수 있는 html을 갖다주기
        form = BlogModelForm()
    return render(request, 'artistapp/post.html', {'form': form})

def write(request):
    if request.method =='POST'or request.method == 'FILES':
        post=Blog()
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.category1=request.POST['category1']
        post.tag=request.POST['tag']
        post.photo=request.FILES.get('photo')
        if request.user.is_authenticated:
            post.user=request.user
        post.date=timezone.now()
        post.save()
        return redirect('/')

    else:
        return render(request, 'artistapp/post.html')

def dongmoon(request):
    print(request.user.university)
    posts = []
    temp_posts=Blog.objects.all()
    for u in  temp_posts:
        print(u.user.university)
        if request.user.university == u.user.university:
            posts.append(u)  
    return render(request, 'artistapp/dongmoon.html',{'posts':posts})


def showprofile(request):
    return render(request, 'artistapp/showprofile.html')

def profilesettings(request):   
    if request.method == 'POST'or request.method == 'FILES':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
          
            profile=request.FILES.get('photo')
            form.save()
            
            return showprofile(request)

    else:
        form = CustomUserChangeForm(instance = request.user)  
                 
        context = {
            'form':form,            
        }    
        return render(request, 'artistapp/profile_settings.html',context)


       