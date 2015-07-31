# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *
from .forms import UploadFileForm
#from django.forms import ModelForm

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
            return HttpResponse("You have registered successfully")
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
    with open('F:/AsiaTube/Video/'+ str(x) + '_'+ f.name, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f

def handle_uploaded_pic(f, x):#'F:/AsiaTube/Video/'+ str(12) + '_' +
    with open('F:/AsiaTube/Icon/'+ str(x) + '_'+ f.name, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f
def uploadvideo(request):
    if 'id' not in request.COOKIES:
        return render_to_response("login.html", context_instance=RequestContext(request))
    if request.method == 'GET':
        return render_to_response("update.html", context_instance=RequestContext(request))
    else:
        if 'file' not in request.FILES:
            return render_to_response("update.html", context_instance=RequestContext(request))
        a = request.FILES['file']
        x = request.COOKIES['id']
        handle_uploaded_file(a, x)
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        #    return HttpResponse("You have upload your file successfully")
        #print(form)
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
        #upload iamge

