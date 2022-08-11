from django.shortcuts import render
from ast import Pass
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    #post요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html')
    #get 요청이 들어오면 login form을 담고 있는 login.html을 띄어주는 역할을 함\
    else:
        return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            #회원가입
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                           )
            #로그인
            auth.login(request, user)
            #홈 리다이렉트
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')