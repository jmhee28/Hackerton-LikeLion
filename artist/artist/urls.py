from django.contrib import admin
from django.urls import path
from artistapp import views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('login/',accounts_views.login, name='login'),

    path('signup/',accounts_views.signup, name='signup'),
    
]
