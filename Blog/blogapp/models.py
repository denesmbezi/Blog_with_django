from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    # Basic post information
    title = models.CharField(
        max_length=200,
        help_text="The title of your blog post"
    )
    
    content = models.TextField(
        help_text="The main content of your blog post"
    )
    
    # Metadata fields
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The author of this post"
    )
    
    created_date = models.DateTimeField(
        default=timezone.now,
        help_text="When the post was created"
    )
    
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text="When the post was published (can be empty for drafts)"
    )
    
    # Optional fields for better blog functionality
    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="URL-friendly version of the title"
    )
    
    # Status choices for draft/published posts
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        help_text="Post status: draft or published"
    )
    
    # For SEO and social sharing
    excerpt = models.TextField(
        max_length=300,
        blank=True,
        help_text="Short description of the post (optional)"
    )
    
    class Meta:
        ordering = ['-created_date']  # Most recent posts first
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL for this post"""
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def publish(self):
        """Method to publish a post"""
        self.published_date = timezone.now()
        self.status = 'published'
        self.save()
    
    @property
    def is_published(self):
        """Check if post is published"""
        return self.status == 'published' and self.published_date is not None