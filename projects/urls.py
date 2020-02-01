from django.urls import path
from . import views
app_name = 'projects'

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('post_detail/<int:pk>/',  views.PostDetailView.as_view(), name = 'post_detail'),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name ='post_delete'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/comment', views.put_comment_on_post, name='comment_create'),
    path('user_posts', views.UserPostView.as_view(), name='user_posts_list'),
    path('post/<int:pk>/funds', views.add_funds_view, name='add_funds')
]