from django.shortcuts import render

# Create your views here.
from homepage.models import MovieModel, BookModel,DirayModel


def movies(request):
    movies = MovieModel.objects.all()
    return render(request, 'moviespage.html', {'movies': movies})
def books(request):
    books = BookModel.objects.all()
    return render(request, 'bookspage.html', {'books': books})
def dirays(request):
    dirays = DirayModel.objects.all()
    return  render(request, 'dirayspage.html', {'dirays':dirays})

