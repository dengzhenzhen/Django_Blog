from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('test', views.test, name='test'),
    path('about', views.index, name='index'),
    path('blog/<int:post_id>', views.post_page, name='post_page')
]
