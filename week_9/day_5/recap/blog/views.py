from django.shortcuts import render
from .models import Blog

# Create your views here.


def index(request):
    blog_queryset = Blog.objects.all().order_by("-created_at")
    # convert to a dict
    blog_list = [blog.__dict__ for blog in blog_queryset]
    context = {"posts": blog_list}
    return render(request, "index.html", context)


def posts(request):
    return render(request, "posts.html")


def authors(request):
    return render(request, "authors.html")
