# blogapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.utils.text import slugify
from .models import Post

def home(request):
    """Display all published posts on the homepage"""
    posts = Post.objects.filter(status='published').order_by('-created_date')
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/home.html', context)

def post_detail(request, slug):
    """Display a single post in detail"""
    post = get_object_or_404(Post, slug=slug, status='published')
    context = {
        'post': post
    }
    return render(request, 'blogapp/post_detail.html', context)

def posts_by_author(request, username):
    """Display all posts by a specific author"""
    author = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=author, status='published').order_by('-created_date')
    context = {
        'posts': posts,
        'author': author
    }
    return render(request, 'blogapp/posts_by_author.html', context)

@login_required
def create_post(request):
    """Create a new blog post (requires login)"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt = request.POST.get('excerpt', '')
        status = request.POST.get('status', 'draft')
        
        if title and content:
            # Create slug from title
            slug = slugify(title)
            
            # Make sure slug is unique
            original_slug = slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            
            # Create the post
            post = Post.objects.create(
                title=title,
                content=content,
                excerpt=excerpt,
                author=request.user,
                slug=slug,
                status=status
            )
            
            if status == 'published':
                post.published_date = timezone.now()
                post.save()
            
            messages.success(request, f'Post "{title}" created successfully!')
            return redirect('blogapp:post_detail', slug=post.slug)
        else:
            messages.error(request, 'Title and content are required.')
    
    return render(request, 'blogapp/create_post.html')

@login_required
def edit_post(request, slug):
    """Edit an existing post (only by author)"""
    post = get_object_or_404(Post, slug=slug)
    
    # Check if user is the author
    if post.author != request.user:
        messages.error(request, "You can only edit your own posts.")
        return redirect('blogapp:post_detail', slug=post.slug)
    
    if request.method == 'POST':
        post.title = request.POST.get('title', post.title)
        post.content = request.POST.get('content', post.content)
        post.excerpt = request.POST.get('excerpt', post.excerpt)
        post.status = request.POST.get('status', post.status)
        
        # Update slug if title changed
        new_slug = slugify(post.title)
        if new_slug != post.slug:
            # Make sure new slug is unique
            original_slug = new_slug
            counter = 1
            while Post.objects.filter(slug=new_slug).exclude(pk=post.pk).exists():
                new_slug = f"{original_slug}-{counter}"
                counter += 1
            post.slug = new_slug
        
        # Set published date if publishing
        if post.status == 'published' and not post.published_date:
            post.published_date = timezone.now()
        
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('blogapp:post_detail', slug=post.slug)
    
    context = {
        'post': post
    }
    return render(request, 'blogapp/edit_post.html', context)

@login_required
def delete_post(request, slug):
    """Delete a post (only by author)"""
    post = get_object_or_404(Post, slug=slug)
    
    # Check if user is the author
    if post.author != request.user:
        messages.error(request, "You can only delete your own posts.")
        return redirect('blogapp:post_detail', slug=post.slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('blogapp:home')
    
    context = {
        'post': post
    }
    return render(request, 'blogapp/confirm_delete.html', context)