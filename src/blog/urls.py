from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="homepage"),
    path('list', views.list_page, name="posts_list_page"),
    path('<slug:post>', views.single_post, name="single_post_page"),
]