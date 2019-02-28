# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views


urlpatterns =[
    url(r'movie/(\d+)', views.movie),
    url(r'music/(\d+)', views.music),
    url(r'book/(\d+)', views.book),
    url(r'diray/(\d+)', views.diray),
    url(r'friend/(\d+)', views.friend),
]
