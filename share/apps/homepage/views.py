from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from homepage.models import MovieModel, MusicModel, BookModel, DirayModel, FriendModel, CallModel


def homepage(request):
    movies = MovieModel.objects.all().order_by('-datemodel_ptr_id')
    books = BookModel.objects.all().order_by('-datemodel_ptr_id')
    musics = MusicModel.objects.all().order_by('-datemodel_ptr_id')
    dirays = DirayModel.objects.all().order_by('-datemodel_ptr_id')
    friends = FriendModel.objects.all().order_by('-datemodel_ptr_id')
    calls = CallModel.objects.all().order_by('-datemodel_ptr_id')
    movies = movies[0]
    books = books[0]
    musics = musics[0]
    dirays = dirays[0]
    friends = friends[0]
    calls = calls[0]

    return render(request, 'homepage.html', locals())
