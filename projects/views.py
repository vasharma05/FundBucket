from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import forms, models
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
# Create your views here.

class PostListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('accounts:login')
    model = models.Post

    def get_queryset(self):
        return models.Post.objects.order_by('-published_date')

class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = models.Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('post_list')
    model = models.Post

class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = forms.PostForm
    model = models.Post
    login_url = reverse_lazy('accounts:login')
    success_url = reverse_lazy('projects:post_detail')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('accounts:login')
    model = models.Post
    success_url = models
    form_class = forms.PostForm


