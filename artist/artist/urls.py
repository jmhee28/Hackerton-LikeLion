from django.contrib import admin
from django.urls import path
from artistapp import views
from accounts import views as accounts_views
from accounts.views import CustomLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/',CustomLoginView.as_view(), name='login'),

    path('signup/',accounts_views.signup, name='signup'),

    path('dongmoon/', views.dongmoon, name ='dongmoon'),

    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('profilesettings/', views.profilesettings, name ='profilesettings'),
    
    path('showprofile/', views.showprofile, name ='showprofile'),
    
    path('write/', views.write, name ='write'),

    path('mypage/', views.mypage, name ='mypage'),
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('create_comment/<int:blog_id>', views.create_comment, name='create_comment'),
]
