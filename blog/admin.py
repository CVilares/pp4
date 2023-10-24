from django.contrib import admin
from.models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin



"""
Registering the Post model in the admin panel
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    """
    Custom Admin panel configuration for the Post model
    """

    """
    Filtering options for the Post list
    """
    list_filter = ('status', 'created_on')

    """
    Enabling the Summernote rich text editor for the 'content' field
    """
    summernote_fields = ('content')

    """
    Generating slugs based on the title
    """
    prepopulated_fields = {'slug': ('title',)}

    """
    Displayed columns in the Post list view
    """
    list_display = ('title', 'slug', 'status', 'created_on')

    """
    Allowing searching by title and content
    """
    search_fields = ['title', 'content']


    @admin.register(Comment)
class PostAdmin(SummernoteModelAdmin):

    list_filter = ('approved', 'created_on')
    summernote_fields = ('content')
    list_display = ('name', 'body', 'post', 'created_on', 'approved') 
    search_fields = ['name', 'email', 'body']