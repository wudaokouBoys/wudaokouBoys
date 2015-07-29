from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from AsiaTube.models import *
from AsiaTube.interface import *
from AsiaTube import *
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