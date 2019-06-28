from django.db import models

# Create your models here.
#post_id、标题topic、 正文text、post时间time
class blog_post(models.Model):
    POST_ID = models.IntegerField(primary_key=True)
    TOPIC = models.CharField(max_length=30)
    TEXT = models.TextField()
    DATE = models.DateField(default='')
    TIME = models.TimeField(default='')