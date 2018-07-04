from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post, Tag


def return_index(request):
    # Get 5 latest posts ordered by date
    all_posts = Post.objects.all().order_by('-created_on')[:5]
    context = {'main_content': all_posts}
    return render(request, 'posts.html', context=context)


def about(request):
    return render(request, 'about.html')


def return_posts_by_tag(request, tag):
    # Get all posts belonging to a specific tag
    tag = tag.lower().replace('%20', ' ')
    found = False
    # todo: instead of query, query it once at server startup and store it in cache
    inner_tags = Tag.objects.all()
    for _tag in inner_tags:
        if tag == _tag.name.lower():
            found = True
            tag = _tag.name
            break
    if not found:
        return HttpResponse(status=501)
    p = Post.objects.all().filter(tag=tag).order_by('-created_on')

    context = {'main_content': p}
    return render(request, 'posts.html', context=context)
