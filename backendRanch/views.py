from django.shortcuts import render


def return_index(request):
    post = {
        'title': 'Post Title',
        'prefix': 'Some introduction here',
        'date': '21/06/2017'
    }
    posts = [post, post, post]
    context = {'main_content': posts}
    return render(request, 'layout.html', context=context)
