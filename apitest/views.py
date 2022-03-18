import pymysql
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import  login_required
from django.contrib import  auth
from apitest.models import Apitest,Apistep,Apis
from django.contrib.auth import authenticate,login

# Create your views here.

def test(request):
    return HttpResponse("hello word")


#登录
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/product_manage/')
            return response
        else:
            return render(request,'login.html',{'error':'username or password error'})

    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

#登出
def logout(request):
    auth.logout(request)
    return render(request,'login.html')

#流程接口基本信息
@login_required
def apitest_manage(request):
    #读取所有流程接口的数据
    apitest_list = Apitest.objects.all()
    #读取浏览器登录session
    username = request.session.get('user','')
    #定义数据变量返回前端
    return render(request,'apitest_manage.html',{'user':username,'apitests':apitest_list})


#流程接口步骤信息
@login_required
def apistep_manage(request):
    username = request.session.get('user','')
    apistep_list = Apistep.objects.all()
    return render(request,'apistep_manage.html',{'user':username,'apisteps':apistep_list})


#单一接口步骤信息
@login_required
def apis_manage(request):
    username = request.session.get('user','')
    apis_list = Apis.objects.all()
    return render(request,'apis_manage.html',{'user':username,'apiss':apis_list})

#测试报告
@login_required
def  test_report(request):
    username = request.session.get('user','')
    apis_list = Apis.objects.all()
    #统计总用例数
    apis_count = Apis.objects.all().count()
    #创建数据库连接
    db = pymysql.connect(user='root',db='autotest',passwd='123456',host='127.0.0.1')
    #创建游标
    cursor = db.cursor()
    sql1= 'select count(id) from apitest_apis where apitest_apis.apistatus=1'
    #执行sql
    aa = cursor.execute(sql1)
    apis_pass_count =[row[0] for row in cursor.fetchmany(aa)][0]
    sql2='select count(id) from apitest_apis where apitest_apis.apistatus=0'
    bb=cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    db.close()
    return render(request,'report.html',{'user':username,'apiss':apis_list,'apiscounts':apis_count,'apis_pass_counts':
                                         apis_pass_count,'apis_fail_counts':apis_fail_count})
