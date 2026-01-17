from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

from .forms import AuthorForm, CategoryForm, PostForm, SearchForm

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            form = AuthorForm()  # limpa o form
    else:
        form = AuthorForm()
    return render(request, 'posts/form_author.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryForm()
    else:
        form = CategoryForm()
    return render(request, 'posts/form_category.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
    else:
        form = PostForm()
    return render(request, 'posts/form_post.html', {'form': form})

def search_post(request):
    results = []
    form = SearchForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Post.objects.filter(title__icontains=query)
    return render(request, 'posts/search.html', {'form': form, 'results': results})
