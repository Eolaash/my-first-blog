from django.shortcuts import render
from django.utils import timezone

# Точка перед models означает текущую директорию или текущее приложение.
from .models import Post 

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
