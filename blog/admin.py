from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
    PostAdmin class inherits from SummernoteModelAdmin class.
    This class is used to customize the Post model in the admin panel.
    The Post model is registered with the PostAdmin class.
    
    The PostAdmin class has the following attributes:
    '''

    list_display = ('title', 'slug', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status','created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)