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
            response = render_to_response("video.html",{}, context_instance=RequestContext(request))
            response.set_cookie('id', id)
            response.set_cookie('videoId', 4)
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
    if 'videoId' not in request.COOKIES:
        return HttpResponse('404 not found')
    videoId = request.COOKIES['videoId']
    ivideo = IVideo()
    video = ivideo.SelectById(videoId)
    if video == None:
        return HttpResponse('404 not found')


    if request.method == 'GET':
        iuser = IUser()
        user = iuser.SelectById(video.upper)
        ivideo.AddPlaynum(videoId)
        print(video.discribe)
        print(82923696)
        return render_to_response("video.html", {
            'Video_title':video.title,
            'VideoUpper':user.name,
            'UpperImage':user.image,
            'Video_uptime':video.time,
            'Playnum':video.playnum,
            'LikeNum':video.likenum,
            'Video_src':video.path,
            'VideoDiscription':video.discribe,
            'BulletScreens':CBulletscreen.objects.filter(video=videoId),
            'videoType':CType.objects.filter(id=video.type)[0].content,
        }, context_instance=RequestContext(request))
    else:
        if 'likeit' in request.POST:
            response_dict = {}
            response_dict.update({'likenum':video.likenum+1})
            ivideo.AddLikenum(videoId)
            return JsonResponse(response_dict)
        else:
            if 'bullettime' in request.POST:
                ibscreen = IBulletscreen()
                newbscreen = CBulletscreen(
                    id = ibscreen.GetlastBsreenId() + 1,
                    video = request.COOKIES['videoId'],
                    time = request.POST['bullettime'],
                    content = request.POST['bulletcontent'],
                )
                ibscreen.Insert(newbscreen)
                ivideo.UpdateBsreen(request.COOKIES['videoId'], newbscreen)
                allthebullets = CBulletscreen.objects.filter(video = request.COOKIES['videoId']).order_by('id')
                response_dict = {}

                return JsonResponse(response_dict)
            else:
                return HttpResponse('传输中网络中断。。')


