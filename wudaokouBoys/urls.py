"""wudaokouBoys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
#from django.contrib import admin
from AsiaTube import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', 'AsiaTube.views.SignUp', name='SignUp'),
    url(r'^upload/$', 'AsiaTube.views.uploadvideo', name = 'uploadvideo'),
    url(r'^login/$', 'AsiaTube.views2.Login', name='Login'),
    url(r'^modifyInfo/$', 'AsiaTube.views.ModifyInfo', name='ModifyInfo'),
    url(r'^modifyPassword/$', 'AsiaTube.views2.ModifyPassword', name='ModifyPassword'),
    url(r'^manageUser/$', 'AsiaTube.views2.manageUser', name='manageUser'),
    url(r'^manageVideo/$', 'AsiaTube.views.manageVideo', name='manageVideo'),
    url(r'^videoPlayer/$', 'AsiaTube.views2.videoPlayer', name='videoPlayer'),
    url(r'^searchResult/$', 'AsiaTube.views.searchResult', name='searchResult'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





