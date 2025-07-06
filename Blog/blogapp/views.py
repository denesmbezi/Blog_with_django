from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    post=Post.objects.all()
    context = {
        'posts': post
    }

    return render(request, 'blogapp/home.html', context)