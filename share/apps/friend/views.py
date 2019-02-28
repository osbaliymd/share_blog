from datetime import date, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from homepage.models import FriendModel



def friend(request):
    if request.method == 'GET':
        # url = reverse('friend')
        return render(request, 'friend.html')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        wechat = request.POST['wechat']
        msg = request.POST['msg']


        if name and email and wechat and msg != '' :

            msg_model = FriendModel()
            msg_model.friend_name = name
            msg_model.friend_email = email
            msg_model.friend_wechat = wechat
            msg_model.friend_comment= msg
            msg_model.time =datetime.now()
            msg_model.save()
            return redirect('/homepage/')
        else:

            return render(request, '404.html', status=404)











