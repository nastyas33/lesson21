from django.http import HttpResponse
from django.views.generic import ListView

from .models import Page, Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

#class PostListView(ListView):
    #model = Post
    #template_name = "all_posts.html"


#class PostCreateView(CreateView):
    #model = Post
    #fields = ["name", "content", "page"]
    #template_name = "post_create.html"
    #success_url = "/"


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["name", "content"]
    success_url = "/"


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = "/"


class PageCreateView(CreateView):
    model = Page
    fields = ["title", "description", "owner"]
    template_name = "page_create.html"
    success_url = "/"


class PageDetailView(DetailView):
    model = Page
    template_name = "page_detail.html"


class PageUpdateView(UpdateView):
    model = Page
    template_name = "page_update.html"
    fields = ["title", "description"]
    success_url = "/"


class PageDeleteView(DeleteView):
    model = Page
    template_name = "page_delete.html"
    success_url = "/"


