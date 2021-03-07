from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['ctime', 'title', 'short_description', 'content',
                    'image', 'slug']



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['ctime', 'content']