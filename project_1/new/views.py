from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from new.models import NewsModel
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsList(ListView):
    model=NewsModel
    template_name='new.html'

class NewsDetail(DetailView):
    model=NewsModel
    template_name='detail.html'

class NewsCrate(LoginRequiredMixin, CreateView):
    model = NewsModel
    fields = ['title', 'body', 'img']
    template_name = 'create.html'
    success_url = reverse_lazy('new')
    login_url = '/admin/login/'

class NewsUpdate(LoginRequiredMixin, UpdateView):
    model = NewsModel
    fields = ['title', 'body', 'img']
    template_name = 'create.html'
    success_url = reverse_lazy('new')
    login_url = '/admin/login/' 

class NewsDelete(LoginRequiredMixin, DeleteView):
    model = NewsModel
    template_name = 'delete.html'
    success_url = reverse_lazy('new')
    login_url = '/admin/login/'