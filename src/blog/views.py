from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Comment
from .forms import NewCommentForm

def home(request):
    kw = {}
    # defining template
    template = 'index.html'
    # getting data
    last_posts = Post.objects.order_by('-ctime')[:5]
    # ok
    kw['posts'] = last_posts
    return render(request, template, kw)


def list_page(request):
    kw = {}
    #defining template
    template = 'list_page.html'
    # getting data
    all_posts = Post.objects.order_by('-ctime').all()
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