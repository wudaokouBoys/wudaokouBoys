# -*- coding=utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *

def Login(request):  #用户登录
    if request.method == 'GET':
        print(request.COOKIES)
        print(88)
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
