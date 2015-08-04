# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *
from .forms import UploadFileForm
#from django.forms import ModelForm
from urllib.parse import unquote
from django.http import JsonResponse
import time

# Create your views here.

def SignUp(request):
    if request.method == 'GET':
        return render_to_response("register.html", context_instance=RequestContext(request))
    else:
        nick_name = request.POST.get("nick-name")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        email = request.POST.get("e-mail")
        a = IUser()
        person = CUser(
            id = a.GetlastUserId() + 1,
            name = nick_name,
            password = password,
            email = email,
            image = "",
            likenum = 0,
            uphistory = "",
            viewhistory = "",
            follow = "",
            followme = "",
            admin = 0
        )
        if (password == password1 and password != ''):
            a.Insert(person)
            response = HttpResponse("You have registered successfully")
            response.set_cookie('id', id)
            return response
        else:
            return render_to_response("register.html",{
                'oldname':nick_name,
                'oldemail':email
            }, context_instance=RequestContext(request))


def handle_uploaded_file(f, x):#'F:/AsiaTube/Video/'+ str(12) + '_' +
    with open('F:/AsiaTube/Video/'+ str(x) + '_v.'+ f.name.split('.')[-1], 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

def handle_uploaded_pic(f):#'F:/AsiaTube/Video/'+ str(12) + '_' +
    with open('F:/AsiaTube/Icon/' + f.name, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

def uploadvideo(request):
    #response = render_to_response("")
    if 'id' not in request.COOKIES:#用户没有登录
        return render_to_response("login.html", context_instance=RequestContext(request))
    itype = IType()
    if request.method == 'GET':
        return render_to_response("update.html",{
            'Types':itype.SelectAllType()
        }, context_instance=RequestContext(request))
    else:
        if 'file' not in request.FILES:
            return render_to_response("update.html", {
                'Types':itype.SelectAllType()
            }, context_instance=RequestContext(request))

        m_title = request.POST['VideoTitle']
        m_discription = request.POST['VideoDiscribe']
        if m_title == '' or m_discription == '' or 'choosedType' not in request.COOKIES:
            return render_to_response("update.html", {
                'VideoTitle':m_title,
                'VideoDiscribe':m_discription,
                'Types':itype.SelectAllType(),
            }, context_instance=RequestContext(request))

        a = request.FILES['file']
        x = request.COOKIES['id']
        ivideo = IVideo()
        m_video_id = ivideo.GetlastVideoId() + 1
        newvideo = CVideo(
            id = m_video_id,
            title = m_title,
            discribe = m_discription,
            keyword = "",
            type = request.COOKIES['choosedType'],
            upper = x,
            time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            path = str(m_video_id)+"_v."+a.name.split('.')[-1],
            state = 0,
            comments = "",
            bsreen = "",
            likenum = 0,
            playnum = 0,
        )
        ivideo.Insert(newvideo)
        x = m_video_id
        handle_uploaded_file(a, x)

        response =  HttpResponseRedirect('/')
        return response

def ModifyInfo(request):
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    id = request.COOKIES['id']
    iuser = IUser()
    user = iuser.SelectById(id)
    if user == None:
        return HttpResponse("You have been deleted")
    if request.method == 'GET':
        return render_to_response("modifyinfo.html", {
            'UserID':id,
            'oldname':user.name,
            'oldemail':user.email,
        },context_instance=RequestContext(request))
    else:
        nick_name = request.POST.get("nick-name")
        email = request.POST.get("e-mail")
        a = IUser()
        a.ModifyEmail(id, email)
        a.ModifyName(id, nick_name)
        if 'file' not in request.FILES:
            return HttpResponse("you have modified your information except for your image")
        file = request.FILES['file']
        suffix = file.name.split('.')[-1]
        file.name = str(id) +'.' +  suffix
        a.ModifyImg(id, file.name)
        handle_uploaded_pic(file)
        return HttpResponse("You have modified successfully!1")
        #upload image

def manageVideo(request):#管理员审查视频界面
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    id = request.COOKIES['id']
    iuser = IUser()
    user = iuser.SelectById(id)
    if user == None:
        return HttpResponse("You have been deleted")
    if user.admin == 0:
        return HttpResponse("You have no right to visit this page!!!")
    ivideo = IVideo()
    videonum = ivideo.GetUnckeckVideoNum()
    if videonum == 0:
        return HttpResponse("No video to be checked, go to sleep.")
    firstvideo_id = ivideo.GetUnckeckVideo()
    ivideo = IVideo()
    video = ivideo.SelectById(firstvideo_id)
    upper_id = video.upper
    upper = iuser.SelectById(upper_id)
    response = render_to_response("managevideo.html" ,{
        'manager_image':user.image,
        'manager':user.name,
        'video_title':video.title,
        'video_discription':video.discribe,
        'video_upper':upper.name,
        'x':videonum,
    }, context_instance=RequestContext(request))
    if request.method == 'GET':
        return response
    else:
        if request.method == 'POST':
        #异常处理
            if 'id' not in request.COOKIES:
                return render_to_response("login.html", context_instance=RequestContext(request))
            id = request.COOKIES['id']
            iuser = IUser()
            user = iuser.SelectById(id)
            if user == None:
                return HttpResponse("You have been deleted")
            if user.admin == 0:
                return HttpResponse("You have no right to visit this page!!!")
            #异常处理
            if request.COOKIES['checkstate'] == '-1':
                print("你没有检查视频！！")
                return response
            if request.COOKIES['checkstate'] == '1':
                print("你允许了视频.")
                ivideo.ModifyState(video.id, 1)#设置数据库里的数据
                iuser.UpdateUphistory(video.upper, video.id, 'add')
                iuser = IUser()
                videonum = ivideo.GetUnckeckVideoNum()
                if (videonum == 0):
                    return HttpResponse("所有视频都审查结束了，你可以睡觉了")
                firstvideo_id = ivideo.GetUnckeckVideo()
                ivideo = IVideo()
                video = ivideo.SelectById(firstvideo_id)
                upper_id = video.upper
                upper = iuser.SelectById(upper_id)
                response.set_cookie('checkstate', -1)#check = -1 未检查 check = 1通过 check=0 拒绝
                return response
            if request.COOKIES['checkstate'] == '0':
                print("你删除了视频！")
                ivideo.Delete(video.id)
                response.set_cookie('checkstate', -1)#check = -1 未检查 check = 1通过 check=0 拒绝
                return response
            print("asdfg")
            return HttpResponse("shenmedongxi?")


def searchResult(request):
    if request.method == 'GET':
        path = request.get_full_path()
        pos1 = (path.find("condition="))
        pos2 = path.find(';')
        pos3 = path.find("content=")
        condition = path[pos1+10:pos2]
        content = unquote(path[pos3+8:len(path)])
        ivideo = IVideo()
        tcontent = ''
        if condition == "keyword":
            tcontent = content
        return render_to_response("search.html", {
            'SearchTarget':tcontent,
            'Videos':ivideo.Search(condition, content)
        },context_instance=RequestContext(request))

def mainPage(request):
    if request.method == 'GET':
        return render_to_response("index.html", {
        },context_instance=RequestContext(request))

def upHistory(request):
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    id = request.COOKIES['id']
    iuser = IUser()
    user = iuser.SelectById(id)
    if user == None:
        return HttpResponse("用户不存在")
    if request.method == 'GET':
        videos = CVideo.objects.filter(upper=id)
        videoList = []
        for video in videos:
            videoItem = {
                'Image':'',
                'id':video.id,
                'title':video.title,
                'playnum':video.playnum,
                'likenum':video.likenum
            }
            videoList.append(videoItem)
        return render_to_response("uphistory.html", {
            'UserImage':user.image,
            'UserName':user.name,
            'Videos':videoList
        },context_instance=RequestContext(request))

def viewHistory(request):
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    id = request.COOKIES['id']
    iuser = IUser()
    user = iuser.SelectById(id)
    if user == None:
        return HttpResponse("用户不存在")
    if request.method == 'GET':
        viewList = AnalysisString(user.viewhistory)
        Videos = []
        ivideo = IVideo()
        for view in viewList:
            video = ivideo.SelectById(view)
            upper = iuser.SelectById(video.upper)
            type = CType.objects.filter(id=video.type)[0].content
            video = {
                'image':'',
                'type':type,
                'id':video.id,
                'title':video.title,
                'upper':user.name,
                'time':video.time,
                'playnum':video.playnum,
                'likenum':video.likenum,
                'comment':len(CComment.objects.filter(video=video.id)),
                'BScreen':len(CBulletscreen.objects.filter(video=video.id)),
            }
            Videos.append(video)
        return render_to_response("viewhistory.html", {
            'Videos':Videos
        },context_instance=RequestContext(request))