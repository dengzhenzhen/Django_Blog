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

    def get_index_data(self):
        posts = blog_post.objects.all()
        data ={
            'data' : [{
                "topic":post.TOPIC,
                 "date":str(post.DATE),
              "post_id":post.POST_ID
                } for post in posts]     
        }   
        return data

    def get_post_data_by_postid(self, post_id):
        '''
        If post_id exists, return query 'select * where POST_ID=post_id'
        else, return False
        '''
        try:
            post = blog_post.objects.get(POST_ID=post_id)
        except:
            return False
        data = {
                'data':{
                        'post_id':post.POST_ID,
                        'topic':post.TOPIC,
                        'date':str(post.DATE),
                        'text':post.TEXT
                        }
                }
        return data       



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

    def get_blog_information(self):
        info = blog_information.objects.get()
        data = {
                'data' : {
                          'blog_name' : info.BLOG_NAME,
                      'home_subtitle' : info.HOME_SUBTITLE,
                     'about_subtitle' : info.ABOUT_SUBTITLE,
                  'self_introduction' : info.SELF_INTRODUCTION,
                        'home_bg_img' : info.HOME_BG_IMG,
                       'about_bg_img' : info.ABOUT_BG_IMG
                }
                }
        return data