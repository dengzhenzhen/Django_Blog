from django.db import models

# Create your models here.

class blog_post(models.Model):
    '''
        POST_ID、标题TOPIC、 正文TEXT、时间DATE 、TIME
    '''
    POST_ID = models.IntegerField(primary_key=True)
    TOPIC = models.CharField(max_length=30)
    TEXT = models.TextField()
    DATE = models.DateField(default='')
    TIME = models.TimeField(default='')
    SUBTITLE = models.CharField(max_length=30, default='')
    BACKGROUND_IMG = models.CharField(max_length=50, default='')

class blog_information(models.Model):
    '''
    BLOG_NAME : Name of your blog, written on homepage.
    HOME_SUBTITLE : Subtitle below blog name.
    ABOUT_SUBTITLE : Subtitle below about
    SELF_INTRODUCTION : Introduction written by markdown.
    HOME_BG_IMG ABOUT_BG_IMG : Background image path.
    '''
    BLOG_NAME = models.CharField(max_length=20)
    HOME_SUBTITLE = models.CharField(max_length=30)
    ABOUT_SUBTITLE = models.CharField(max_length=30)
    SELF_INTRODUCTION = models.TextField()
    HOME_BG_IMG = models.CharField(max_length=30)
    ABOUT_BG_IMG = models.CharField(max_length=30)

