from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from Webtest.models import Webcase,Webcasestep
# Create your views here.

@login_required
def webcase_manage(request):
    username = request.session.get('user','')
    webcase_list = Webcase.objects.all()
    return render(request,'webcase_manage.html',{'user':username,'webcases':webcase_list})


@login_required
def webcasestep_manage(request):
    username = request.session.get('user','')
    webcasestep_list = Webcasestep.objects.all()
    return  render(request,'webcasestep_manage.html',{'user':username,'webcasesteps':webcasestep_list})
