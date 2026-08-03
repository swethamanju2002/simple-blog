from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BlogPost
from .forms import BlogPostForm


def home(request):
    """Display all blog posts on the home page."""
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


def create_post(request):
    """Create a new blog post."""
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Blog post created successfully!')
                return redirect('home')
            except Exception as e:
                print(e)
                raise
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
        'title': 'Create Blog Post'
    })


def post_detail(request, pk):
    """Display the full details of a single blog post."""
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def edit_post(request, pk):
    """Edit an existing blog post."""
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
        'title': 'Edit Blog Post'
    })


def delete_post(request, pk):
    """Delete a blog post after confirmation."""
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


def search_posts(request):
    """Search blog posts by title only."""
    query = request.GET.get('q', '').strip()
    posts = BlogPost.objects.filter(title__icontains=query) if query else BlogPost.objects.none()
    return render(request, 'blog/search_results.html', {
        'posts': posts,
        'query': query
    })


def about(request):
    """Static About page."""
    return render(request, 'blog/about.html')


def contact(request):
    """Static Contact page."""
    return render(request, 'blog/contact.html')
