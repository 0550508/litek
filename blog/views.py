from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User


def create100(requests):
    me = User.objects.get(username='admin')
    for i in range(100):
        p=Post.objects.create(author=me, title=f'footbal_omid {i}', text=f'footbal_omid dar barabare hongkong baxte{i}')
        p.publish()
    return HttpResponse('done')