from django.urls import path
from . import views
app_name = 'projects'

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name = 'post_list'),
    path('post_detail/<int:pk>/',  views.PostDetailView.as_view(), name = 'post_detail'),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name ='post_delete'),
    path('post_create/', views.PostCreateView.as_view(), name='post_create')
]