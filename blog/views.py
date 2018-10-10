from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def listar(request):
    posts = Post.objects.all()
    return render(request, 'blog/listar.html', {'posts':posts})
