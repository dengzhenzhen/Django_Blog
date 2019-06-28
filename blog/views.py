from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import blog_post
import json
# Create your views here.

def index(request):
    posts = blog_post.objects.all()
    # topics = [post.TOPIC for post in posts]
    # dates =  [str(post.DATE) for post in posts]
    # post_ids = [post.POST_ID for post in posts]
    # useless now 2019-06-28
    data = [{
        "topic":post.TOPIC,
         "date":str(post.DATE),
      "post_id":post.POST_ID
            } for post in posts]
    context = {'DATA' : data}
    #print(context)
    #return HttpResponse(context)
    return render(request, 'blog/index.html', context=context)

def post_page(request, post_id):
    try:
        post = blog_post.objects.get(POST_ID=post_id)
    except:
        #跳到404页面
        return HttpResponseNotFound(content='url not found')
    data = {
            'data':{
                    'post_id':post.POST_ID,
                      'topic':post.TOPIC,
                       'date':str(post.DATE),
                       'text':post.TEXT
                    }
            }
    return render(request, 'blog/post.html', context=data)

def test(request):

    return render(request, 'blog/test.html')
