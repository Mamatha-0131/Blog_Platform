from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('home')
    return render(request, 'create_post.html')

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        text = request.POST['text']
        Comment.objects.create(post=post, user=request.user, text=text)
        return redirect('home')
