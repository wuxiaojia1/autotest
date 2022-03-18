"""autotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from apitest import views
from product import proviews
from bug import bugviews
from set import setviews
from Webtest import webviews


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'test/',views.test),
    path(r'login/',views.login,name='login'),
    path(r'home/',views.home),
    path(r'logout/',views.logout),
    path(r'product_manage/',proviews.product_manage),
    path(r'apitest_manage/',views.apitest_manage),
    path(r'apistep_manage/',views.apistep_manage),
    path(r'apis_manage/',views.apis_manage),
    path(r'bug_manage/',bugviews.bug_manage),
    path(r'set_manage/',setviews.set_manage),
    path(r'set_user_manage/',setviews.set_user_manage),
    path(r'webcase_manage/',webviews.webcase_manage),
    path(r'webcasestep_manage/',webviews.webcasestep_manage),
    path(r'report/',views.test_report)



]
