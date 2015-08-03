# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *
from .forms import UploadFileForm
#from django.forms import ModelForm
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

       # p = person(
       #     name=person_name,
       #     id=person_id,
        #    job=person_job,
       #     pay=person_pay
     #   )
     #   p.save()

def handle_uploaded_file(f, x):#'F:/AsiaTube/Video/'+ str(12) + '_' +
    with open('F:/AsiaTube/Video/'+ str(x) + '_v.'+ f.name.split('.')[-1], 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

def handle_uploaded_pic(f, x):#'F:/AsiaTube/Video/'+ str(12) + '_' +
    with open('F:/AsiaTube/Icon/'+ str(x) + '_'+ f.name, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

def uploadvideo(request):
    #response = render_to_response("")
    if 'id' not in request.COOKIES:#用户没有登录
        return render_to_response("login.html", context_instance=RequestContext(request))
    if request.method == 'GET':
        itype = IType()
        return render_to_response("update.html",{
            'Types':itype.SelectAllType()
        }, context_instance=RequestContext(request))
    else:
        if 'file' not in request.FILES:
            return render_to_response("update.html", context_instance=RequestContext(request))
        a = request.FILES['file']
        x = request.COOKIES['id']
        ivideo = IVideo()
        m_video_id = ivideo.GetlastVideoId() + 1
        m_title = request.POST['VideoTitle']
        m_discription = request.POST['VideoDiscribe']
        newvideo = CVideo(
            id = m_video_id,
            title = m_title,
            discribe = m_discription,
            keyword = "",
            type = 1,
            upper = x,
            time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            path = str(m_video_id)+"_v."+a.name.split('.')[-1],
            state = 0,
            comments = "",
            bsreen = "",
            likenum = 0,
            playnum = 0,
        )
        print(newvideo.path)
        print('asdfg')
        ivideo.Insert(newvideo)
        x = m_video_id
        handle_uploaded_file(a, x)
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        #    return HttpResponse("You have upload your file successfully")
        #print
        #print(form.title)

        return render_to_response("video.html",{
            'UserID':x,
            'Video_title':'萌杰打飞机',
            'Video_src':'http://192.168.1.103:8000/static/1.mp4'
        }, context_instance=RequestContext(request))

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
        a.ModifyImg(id, file.name)
        handle_uploaded_pic(file, id)
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
    iuser = IUser()
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