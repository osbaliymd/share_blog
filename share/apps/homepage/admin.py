from django.contrib import admin
#
# Register your models here.
from .models import BookModel, MovieModel, MusicModel, DateModel, ChatModel, DirayModel, FriendModel, CallModel

#
# class AdminMoudle(admin.ModelAdmin):
#     list_display = ('music_name', 'book_name', 'movie_name','time')
#
#
#
admin.site.register(MovieModel)
admin.site.register(MusicModel)
admin.site.register(BookModel)
admin.site.register(ChatModel)
admin.site.register(DirayModel)
admin.site.register(DateModel)
admin.site.register(FriendModel)
admin.site.register(CallModel)
