from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from homepage.models import MovieModel, MusicModel, BookModel, DirayModel, FriendModel


def movie(request, con_id):
    movie = MovieModel.objects.get(pk=con_id)
    return render(request, 'sharecontent.html', {'movie': movie})

def music(request, con_id):
    music = MusicModel.objects.get(pk=con_id)
    return render(request, 'sharecontent.html', {'music': music})


def book(request, con_id):
    book = BookModel.objects.get(pk=con_id)
    return render(request, 'sharecontent.html', {'book': book})

def diray(request,con_id):
    diray = DirayModel.objects.get(pk =con_id)
    return render(request, 'sharecontent.html', {'diray': diray})
def friend(request,con_id):
    friend = FriendModel.objects.get(pk =con_id)
    return render(request,'sharecontent.html', {'friend': friend})