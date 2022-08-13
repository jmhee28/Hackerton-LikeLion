from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import *

class UserAdmin(BaseUserAdmin):
    # 관리자 화면에 보여질 칼럼 지정
    list_display = ('username','email','is_admin','is_staff', 'university', 'major', 'careerInterest','is_student','is_looking_job','is_headhunter')
    search_fields = ('username', 'name','email')
    readonly_fields = ('id', 'create_dt', 'last_login')

    list_filter = ('is_admin',)
    ordering = ()
    fieldsets = ()
    filter_horizontal = ()


# Photo 클래스를 inline으로 나타낸다.
class PhotoInline(admin.TabularInline):
    model = Photo

# Post 클래스는 해당하는 Photo 객체를 리스트로 관리하는 한다. 
class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Blog, PostAdmin)
admin.site.register(CategoryTree)
admin.site.register(Comment)
admin.site.register(Individual_info)
