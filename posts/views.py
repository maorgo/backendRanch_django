from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'layout.html')


def posts(request):
    # Get all posts ordered by date descending
    posts_with_tags = {}
    all_posts = Post.objects.all().order_by('-created_on')
    for post in all_posts:
        posts_with_tags.update({post: post.tags.names()})
    context = {'main_content': posts_with_tags}
    return render(request, 'posts.html', context=context)


def get_post(request, slug):
    # Get a specific post by it's slug (made out of the title)
    requested_post = Post.objects.get(slug=slug)
    tags = requested_post.tags.names()
    context = {'post': requested_post,
               'tags': tags}
    return render(request, 'post.html', context=context)
#
