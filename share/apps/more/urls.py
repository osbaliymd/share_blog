# -*- coding: utf-8 -*-
from django.conf.urls import url

from more import views

urlpatterns =[
    url(r'^movies/', views.movies),
    url(r'^books/', views.books),
    url(r'^dirays/',views.dirays),

]