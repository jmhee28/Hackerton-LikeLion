from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserForm(UserCreationForm):
    email = forms.EmailField(label="email")
    major = forms.CharField(label = "major")
    university = forms.CharField(label = "university")
    
    class Meta:
        model = User
        fields = ("university", "major","username", "email", "address", "phone_number","is_student","is_looking_job","is_headhunter","careerInterest")

class CustomUserChangeForm(forms.ModelForm):
 
    password = None
    class Meta:
        model =  User
        fields = ("university", "major","username", "email", "address", "phone_number","is_student","is_looking_job","is_headhunter","careerInterest")



class BlogForm(forms.Form):
    #내가 입ㄱ력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']       