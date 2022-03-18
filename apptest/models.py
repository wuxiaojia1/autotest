from django.db import models

# Create your models here.
class Appcase(models.Model):
    Products = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    appcasename = models.CharField('测试用例',max_length=200)
    apptestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间',auto_now=True)
    class Meta:
        verbose_name = 'app测试用例'
        verbose_name_plural = 'app测试用例'
    def __str__(self):
        return self.appcasename


class Appcasestep(models.Model):
    Appcase = models.ForeignKey(Appcase,on_delete=models.CASCADE)
    appteststep = models.CharField('测试步骤',max_length=200)
    apptestobjname = models.CharField('测试对象名称描述',max_length=200)
    appfindmethod = models.CharField('定位方法',max_length=200)
    appvelement = models.CharField('控件元素',max_length=800)
    appoptmethod = models.CharField('操作方法',max_length=200)
    apptestdata = models.CharField('测试数据',max_length=200,null=True)
    appassertdata = models.CharField('验证数据',max_length=200)
    apptestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间',auto_now=True)
    def __str__(self):
        return self.appteststep