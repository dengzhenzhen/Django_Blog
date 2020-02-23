from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from .models import blog_post, blog_information
import json
# Create your views here.

def index(request):
    # return render(request, 'blog/index.html', context=blog_post().get_index_data())
    # When using Vue as frontend, DO NOT use render, because there are conflicts between their programmers.
    with open("D:/Repositories/Django_Blog/blog/templates/blog/index.html", 'rb') as fp:
        tmp = fp.read()
    return HttpResponse(tmp)

def post_page(request, post_id):
    data = blog_post().get_post_data_by_postid(post_id)
    # return render(request, 'blog/post.html', context=data) if data else HttpResponseNotFound()
    return JsonResponse(data) if data else HttpResponseNotFound()


def about_page(request):
        return render(request, 'blog/about.html', context=blog_information().get_blog_information())

def test(request):
    data = blog_post().get_index_data()
    # return render(request, 'blog/test.html')
    # return HttpResponse(json.dumps(data),content_type="application/json")
    return JsonResponse(data) if data else HttpResponseNotFound()

def resume(request):
    path = "D:/Repositories/Resume/resume.md"
    with open(path, mode='r', errors='ignore', encoding='utf-8') as fp:
        data = {'data':{"text":fp.read()}}
    return render(request, 'blog/resume.html', context=data)