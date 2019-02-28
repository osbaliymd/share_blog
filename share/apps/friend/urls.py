# -*- coding: utf-8 -*-


from django.conf.urls import url

from friend import views

urlpatterns = [
    url(r'^$', views.friend),
    url(r'friend/', views.friend, name='friend'),
    url(r'/friend/formerr/', views.friend,name='friend'),
]