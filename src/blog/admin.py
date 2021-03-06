from django.contrib import admin

from .models import Post, Comment

class PostAdminView(admin.ModelAdmin):

    list_display = ('title', 'ctime', 'slug')


class CommentAdminView(admin.ModelAdmin):

    list_display = ('ctime', 'linked_post')



admin.site.register(Post, PostAdminView)
admin.site.register(Comment, CommentAdminView)