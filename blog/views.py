from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Author,Post,Categoria

# Create your views here.


class PostList(ListView):
    template_name = "blog/blog.html"
    context_object_name = 'posts'
   
    queryset = Post.objects.all()
    

class PostDetail(DetailView):
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Categoria.objects.all()
        return context









        
