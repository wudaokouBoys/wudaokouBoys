from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *

def Login(request):  #ÓÃ»§µÇÂ¼
    if request.method == 'GET':
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
            return HttpResponse("Login successfully")
