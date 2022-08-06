from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Post, Group


def index(request):
    posts = Post.objects.select_related('group')[:settings.POSTS_PER_PAGE]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.group_post.all()[:settings.POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
