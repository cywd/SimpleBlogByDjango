"""simpleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views as blog_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blog_views.post_list, name='blog_post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', blog_views.post_detail, name='blog_post_detail'),
    url(r'^post/new/$', blog_views.post_new, name='blog_post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', blog_views.post_edit, name='blog_post_edit'),
    url(r'^drafts/$', blog_views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', blog_views.post_remove, name='blog_post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', blog_views.post_publish, name='blog_post_publish'),
]
