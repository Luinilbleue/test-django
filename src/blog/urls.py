from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'blog'

router = routers.DefaultRouter()
router.register('posts', views.AllPostsViewSet)
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', views.home, name="homepage"),
    path('list', views.list_page, name="posts_list_page"),
    path('post/<slug:post>', views.single_post, name="single_post_page"),
    path('json_', include(router.urls))
]