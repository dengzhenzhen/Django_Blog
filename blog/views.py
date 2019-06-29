from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import blog_post, blog_information
import json
# Create your views here.

def index(request):

    context = {'DATA' : blog_post().get_index_data()}
    #print(context)
    #return HttpResponse(context)
    return render(request, 'blog/index.html', context=context)

def post_page(request, post_id):
    data = blog_post().get_post_data_by_postid(post_id)
    return render(request, 'blog/post.html', context=data) if data else HttpResponseNotFound()


def about_page(request):
        return render(request, 'blog/about.html', context=blog_information().get_blog_information())

def test(request):

    return render(request, 'blog/test.html')
