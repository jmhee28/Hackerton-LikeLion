from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import *
from django.contrib.auth.forms import UserChangeForm
from django.utils import timezone
from accounts.forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

def chatlist(request):
    users = User.object.all()
    return render(request, 'artistapp/chatlist.html',{'users': users})


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'artistapp/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):#채팅 
    room = request.POST['room_name']
    username =  request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})




#위에는 메시시 함수


def likes(request, article_pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Blog, pk=article_pk)

        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('singlepost',article_pk )
    return redirect('accouts/login.')


def singlepost(request, post_id):       
    single_post = get_object_or_404(Blog, pk=post_id)
    post_comments = Comment.objects.filter(post=post_id)
    post_photos = Photo.objects.filter(post=post_id)

    if post_comments:
        return render(request, 'artistapp/single-post.html', {'single_post':single_post,"post_id":post_id, "post_comments":post_comments, "post_photos": post_photos })
    else:
        return render(request, 'artistapp/single-post.html', {'single_post':single_post, "post_id":post_id, "post_photos": post_photos})

def home(request):
    if not request.user.is_authenticated:
         return render(request, 'accounts/login.html')
    else:
        posts=Blog.objects.filter(user=request.user)
        fields=CategoryTree.objects.all()
        if request.user.is_authenticated:
            info=Individual_info()
            info=Individual_info.objects.filter(user=request.user)
            return render(request, 'artistapp/mainfeed.html',{'fields':fields,'posts':posts,'info':info})
        else:
            return render(request, 'artistapp/mainfeed.html',{'fields':fields,'posts':posts,})

def mypage(request):
     #블로그 글들을 모조리 띄워주는 코드
    #posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('-date')
    return render(request, 'artistapp/mypage.html', {'posts':posts})

def mypage2(request):
    return render(request, 'artistapp/mypage2.html')

def portfolio(request):
    return render(request, 'artistapp/portfolio.html')

def jobhunt(request):
    return render(request, 'artistapp/job-hunt.html')   

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
        #post.tag=request.POST['tag']
        if request.user.is_authenticated:
            post.user=request.user
        post.date=timezone.now()
        post.save()
        for img in request.FILES.getlist('photo'):
            # Photo 객체를 하나 생성한다.
            photo = Photo()
            # 외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = post
            # imgs로부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            # 데이터베이스에 저장
            photo.save()          
        return redirect('/')
        

    else:
        return render(request, 'artistapp/post.html')

def showuserPost(request, user_id):
    user_= get_object_or_404(User, pk=user_id)
    #print(user_i)
    posts=Blog.objects.filter(user=user_)
    fields=CategoryTree.objects.all()    
    info=Individual_info()
    info=Individual_info.objects.filter(user=user_)
    return render(request, 'artistapp/index.html',{'fields':fields,'posts':posts,'info':info})



def dongmoon(request):
    university =request.user.university
    users = []
    other_users = []
    temp_users=get_user_model().object.all()
    print(temp_users.count())
    for u in  temp_users:
        print(u.university)
        if request.user.university == u.university:
            users.append(u)
        else :
            other_users.append(u)  
    return render(request, 'artistapp/동문.html',{'users':users,'university':university, 'other_users':other_users })


def showprofile(request):
    return render(request, 'artistapp/showprofile.html')

def profilesettings(request):   
    if request.method == 'POST'or request.method == 'FILES':
        form = CustomUserChangeForm(request.POST, instance=request.user)
       
        if form.is_valid():
            
            #profile=request.FILES.get('photo')
            form.save()
            print("valid")
            return showprofile(request)

    else:
        form = CustomUserChangeForm(instance = request.user)  
                 
        context = {
            'form':form,            
        }    
        return render(request, 'artistapp/profile_settings.html',context)


       