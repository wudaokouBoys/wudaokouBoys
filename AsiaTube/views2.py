# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *

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
