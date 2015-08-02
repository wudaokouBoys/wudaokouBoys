# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.logic import *
from AsiaTube.models import *
from AsiaTube.interface import *
from django.http import JsonResponse
import json

def Login(request):  #用户登录
    if request.method == 'GET':
        print(request.COOKIES)
        return render_to_response("login.html", context_instance=RequestContext(request))
    else:
        id = request.POST.get('id')
        password = request.POST.get('password')
        iuser = IUser()
        user = iuser.SelectById(id)
        if user == None:
             return render_to_response("login.html",{
            }, context_instance=RequestContext(request))
        elif user.password != password:
             return render_to_response("login.html",{
                 'oldid':id,
            }, context_instance=RequestContext(request))
        else:
            response = HttpResponse()
            response.set_cookie('id', id)
            return response
            #return HttpResponse("Login successfully")

def ModifyPassword(request):
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    id = request.COOKIES['id']
    iuser = IUser()
    user = iuser.SelectById(id)
    if user == None:
        return HttpResponse("User doesn't exist")

    if request.method == 'GET':
        return render_to_response("modifypassword.html", context_instance=RequestContext(request))
    else:
        oldpassword = request.POST.get('password0')
        if oldpassword != user.password:
            return render_to_response("modifypassword.html", context_instance=RequestContext(request))
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            return render_to_response("modifypassword.html", context_instance=RequestContext(request))
        else:
            if password1 == '':
                return render_to_response("modifypassword.html", context_instance=RequestContext(request))
            iuser.ModifyPassword(id, password1)
            return HttpResponse("modify password successfully")

def manageUser(request):
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    id = request.COOKIES['id']
    iuser = IUser()
    manager = iuser.SelectById(id)
    if manager == None:
        return HttpResponse("User doesn't exist")
    if manager.admin != 1:
        return HttpResponse("How can you find  this page!")

    if request.method == 'GET':
        return render_to_response("manageUser.html",{
            'manager_image': manager.image,
            'manager': manager.name,
            'search_result':'none',
        }, context_instance=RequestContext(request))
    elif request.method == 'POST':
        if 'search' in request.POST:
            print(1)
            user_id = request.POST.get('user_id')
            if user_id == '':
                return render_to_response("manageUser.html",{
                'manager_image': manager.image,
                'manager': manager.name,
                'search_result':'none',
            }, context_instance=RequestContext(request))
            user = iuser.SelectById(user_id)
            if user == None or user.admin == 1:
                return render_to_response("manageUser.html",{
                    'manager_image': manager.image,
                    'manager': manager.name,
                    'search_result':'none',
                }, context_instance=RequestContext(request))
            ivideo = IVideo()
            videoList = AnalysisString(user.uphistory)
            videos = []
            for video in videoList:
                videos.append(ivideo.SelectById(video))
            response = render_to_response("manageUser.html",{
            'manager_image': manager.image,
            'manager': manager.name,
            'search_result':'block',
            'user_image':user.image,
            'user_name': user.name,
            'user_id':user.id,
            'user_like':user.likenum,
            'user_followme':len(AnalysisString(user.followme)),
            'videos':videos,
            }, context_instance=RequestContext(request))
            response.set_cookie('manageUser', user.id)

            return response
        elif 'setAdmin' in request.POST:
            user_id = int(request.COOKIES['manageUser'])
            print(manager.id)
            print(user_id)
            print('fiywhfhaeughaweg')
            SetAdmin(manager.id, user_id)
        elif 'deleteUser' in request.POST:
            print(3)
            user_id = request.COOKIES['manageUser']
            DeleteUser(manager.id, user_id)
        return render_to_response("manageUser.html",{
            'manager_image': manager.image,
            'manager': manager.name,
            'search_result':'none',
        }, context_instance=RequestContext(request))


def videoPlayer(request):
    if request.method == 'GET':
        return render_to_response("video.html", {
            'Playnum':1,
            'Video_src':'/static/1.mp4',
        }, context_instance=RequestContext(request))
    else:
        if 'likeit' in request.POST:
            response_dict = {}
            response_dict.update({'likenum':2})
            return JsonResponse(response_dict)
        else:
            print('fuahfha')
            return HttpResponse('haha')

