from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('test', views.test, name='test'),
    # path('about', views.about_page, name='about'),
    # path('blog/<int:post_id>', views.post_page, name='post_page'),
    path('resume', views.resume, name='resume')
]
