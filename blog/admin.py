from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

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
class CommentAdmin(SummernoteModelAdmin):

    """
    Filtering options for the Comment list
    """
    list_filter = ('approved', 'created_on')
    """
    Enabling the Summernote rich text editor for the 'content' field
    """
    summernote_fields = ('content')
    """
    Displayed columns in the Comment list view
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    """
    Allowing searching by name, email, and body
    """
    search_fields = ['name', 'email', 'body']

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Approve user comments method
        """
        queryset.update(approved=True)
