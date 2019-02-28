from django.db import models


# Create your models here.
class DateModel(models.Model):
    time = models.DateTimeField(verbose_name='发布时间')





class MusicModel(DateModel,models.Model):
    music_name = models.CharField(max_length=10, verbose_name='音乐名')
    music_singer = models.CharField(max_length=5, verbose_name='歌手')
    music_img = models.ImageField(upload_to='img', verbose_name='音乐配图')
    music_comment = models.TextField('音乐评论')


    class Meta:
        db_table = 'tb_musics'
        verbose_name = '音乐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.music_name


class BookModel(DateModel, models.Model):

    book_title = models.CharField (max_length=20, verbose_name='标题')
    book_name = models.CharField(max_length=10, verbose_name='书名')
    book_auther = models.CharField(max_length=5, verbose_name='作者')
    book_comment = models.TextField(verbose_name='书评')
    book_img = models.ImageField(upload_to='img', verbose_name='图书配图')

    class Meta:
        db_table = 'tb_books'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.book_title

class MovieModel(DateModel,models.Model):

    movie_title = models.CharField (max_length=20, verbose_name='标题')
    movie_name = models.CharField(max_length=10, verbose_name='电影名称')
    movie_comment = models.TextField(verbose_name='影评')
    movie_img = models.ImageField(upload_to='img', verbose_name='电影配图')
    class Meta:
        db_table = 'tb_movies'
        verbose_name = '电影'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.movie_title
class ChatModel(DateModel, models.Model):

    chat_title = models.CharField (max_length=20, verbose_name='吐槽标签')

    chat_comment = models.TextField(verbose_name='吐槽')
    chat_img = models.ImageField(upload_to='img', verbose_name='吐槽配图')
    class Meta:
        db_table = 'tb_chats'
        verbose_name = '吐槽'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.chat_title

class DirayModel(DateModel,models.Model):

    diray_weather = models.CharField (max_length=10, verbose_name='天气')
    diray_date = models.DateField(verbose_name='日期')
    diray_comment = models.TextField(verbose_name='日记正文')
    diray_img = models.ImageField(upload_to='img', verbose_name='日记配图')
    class Meta:
        db_table = 'tb_dirays'
        verbose_name = '日记'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.diray_date)

class FriendModel(DateModel,models.Model):
    friend_name = models.CharField(max_length=10, verbose_name='昵称')
    friend_email = models.CharField(max_length=20, verbose_name='邮箱')
    friend_wechat = models.CharField(max_length=20, verbose_name='微信')
    friend_comment = models.TextField(verbose_name='留言')

    class Meta:
        db_table = 'tb_friends'
        verbose_name = '朋友'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.friend_name
class CallModel(DateModel , models.Model):
    call_title = models.CharField(max_length=30,verbose_name='公告标题')
    call_comment =models.TextField(verbose_name='公告内容')


    class Meta:
        db_table = 'tb_call'
        verbose_name = '公告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.call_title










