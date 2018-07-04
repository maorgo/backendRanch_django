from django.urls import path, include
from . import views

urlpatterns = [
    path('<slug>', views.get_post, name='get_post'),
    path('', views.posts, name='posts')
]
