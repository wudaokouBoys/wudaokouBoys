# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *
from .forms import UploadFileForm
#from django.forms import ModelForm

# Create your views here.

def register(request):
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
        if (password == password1):
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

def handle_uploaded_file(f):#'F:/AsiaTube/Video/'+ str(12) + '_' +
    with open('F:/AsiaTube/Video/'+ str(12306) + '_'+ f.name, 'wb+') as info:
        for chunk in f.chunks():
            info.write(chunk)
    return f
def uploadvideo(request):
    if request.method == 'GET':
        return render_to_response("update.html", context_instance=RequestContext(request))
    else:
        a = request.FILES['file']
        handle_uploaded_file(a)
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        #    return HttpResponse("You have upload your file successfully")
        #print(form)
        #print(form.title)

        return render_to_response("video.html",{
            'UserID':12306,
            'Video_title':'萌杰打飞机',
            'Video_src':'http://192.168.1.103:8000/static/1.mp4'
        }, context_instance=RequestContext(request))
