from django.shortcuts import render
from set.models import Set
from django.contrib.auth.models import User
# Create your views here.

#系统管理
def set_manage(request):
    username = request.session.get('user','')
    set_list = Set.objects.all()
    return render(request,'set_manage.html',{'user':username,'sets':set_list})

#用户管理
def set_user_manage(request):
    username = request.session.get('user','')
    user_list = User.objects.all()
    return render(request,'set_user_manage.html',{'user':username,'users':user_list})