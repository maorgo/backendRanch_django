from django.shortcuts import render
from taggit.models import Tag
from posts.models import Post

TAGS = Tag.objects.all()


def return_index(request):
    # Get 5 latest posts ordered by date
    all_posts = Post.objects.all().order_by('-created_on')[:5]
    context = {'main_content': all_posts,
               'tags': TAGS}
    return render(request, 'posts.html', context=context)


def about(request):
    context = {'tags': TAGS}
    return render(request, 'about.html', context=context)


def return_posts_by_tag(request, tag):
    # Get all posts belonging to a specific tag
    p = Post.objects.filter(tags__name__in=[tag]).order_by('-created_on')
    context = {'main_content': p,
               'tags': TAGS}
    return render(request, 'posts.html', context=context)
