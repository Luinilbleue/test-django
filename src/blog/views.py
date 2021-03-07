from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment
from .forms import NewCommentForm
from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer

def home(request):
    kw = {}
    # defining template
    template = 'index.html'
    # getting data
    last_posts = Post.objects.order_by('-ctime')[:4]
    # ok
    kw['posts'] = last_posts
    return render(request, template, kw)


def list_page(request):
    kw = {}
    #defining template
    template = 'list_page.html'
    # getting data
    all_posts = Post.objects.all().order_by('-ctime')
    # ok
    kw['posts'] = all_posts
    return render(request, template, kw)


def single_post(request, post):
    kw = {}
    # defining template
    template = 'single_post.html'
    # getting post data
    post = get_object_or_404(Post, slug=post)
    # getting comments data
    comments = post.comments.all()

    user_comment = {}

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.linked_post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    kw['post'] = post
    kw['comments'] = comments
    kw['comment_form'] = comment_form
    return render(request, template, kw)



class AllPostsViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-ctime')
    serializer_class = PostSerializer



class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-ctime')
    serializer_class = PostSerializer
    lookup_field = 'slug'