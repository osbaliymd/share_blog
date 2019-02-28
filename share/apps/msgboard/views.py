from django.shortcuts import render

# Create your views here.
from homepage.models import  FriendModel
def msgboard(request):
    msgs = FriendModel.objects.all().order_by('-datemodel_ptr_id')
    return render(request, 'msgboard.html', {'msgs': msgs})