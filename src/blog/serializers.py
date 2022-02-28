from rest_framework import serializers
from .models import Post, Comment

#serializer pour la class Post
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['ctime', 'title', 'short_description', 'content',
                    'image', 'slug']
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


# not in use at the moment
#serializer pour la class Comment
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['ctime', 'content']