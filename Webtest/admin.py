from django.contrib import admin
from Webtest.models import Webcase,Webcasestep
# Register your models here.

class WebcasestepAdmin(admin.TabularInline):
    list_display = ['webcasename','webteststep','webtestobjname','webfindmethod','webevelement','weboptmethod',
                    'webassertdata','webtestresult','create_time','id','webcase']
    model = Webcasestep
    #默认显示条目的数量
    extra = 1


class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','webtestresult','create_time','id']
    inlines = [WebcasestepAdmin]

admin.site.register(Webcase,WebcaseAdmin)