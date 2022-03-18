from django.contrib import admin
from product.models import Product
from apitest.models import Apitest,Apis
from Webtest.models import Webcase
# Register your models here.

class ApisAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparamvalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1

class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcasename','webtestresult','create_time','id','product']
    model = Webcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','producter','create_time','id']
    inlines = [ApisAdmin,WebcaseAdmin]



#把产品模块注册到django后台并根据字段显示
admin.site.register(Product,ProductAdmin)