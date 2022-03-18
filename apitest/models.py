from django.db import models
from product.models import Product
# Create your models here.
#接口测试基本信息表
class Apitest(models.Model):
    # 关联产品ID，其中product是应用名，product是product的应用表名
    product = models.ForeignKey('product.product',on_delete=models.CASCADE)
    #执行结果数据库表字段
    apitestname = models.CharField('流程接口名称',max_length=64)
    apitestdesc = models.CharField('流程接口描述',max_length=64,null=True)
    apitester = models.CharField('测试负责人',max_length=16)
    apitestresult = models.BooleanField('测试结果')
    create_time = models.DateTimeField('创建时间',auto_now=True)
    class Meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname

#场景测试步骤表
class Apistep(models.Model):
    #接口用例数据库表
    #关联接口ID
    apitest = models.ForeignKey(Apitest,on_delete=models.CASCADE)
    apiname = models.CharField('接口名称',max_length=100)
    apiurl = models.CharField('接口地址',max_length=200)
    apistep = models.CharField('测试步骤',max_length=100,null=True)
    apiparamvalue = models.CharField('请求参数和值',max_length=800)
    REQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    apimethod = models.CharField(verbose_name='请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True)
    apiresult = models.CharField('预期结果',max_length=200)
    apistep = models.CharField('测试步骤',max_length=100,null=True)
    apistatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间',auto_now=True)

    def __str__(self):
        return self.apiname


#单一场景测试接口表
class Apis(models.Model):
    #外键，关联产品表id
    Rroduct = models.ForeignKey('product.product',on_delete=models.CASCADE)
    #各表字段
    apiname = models.CharField('接口名称',max_length=100)
    apiurl = models.CharField('接口地址', max_length=200)
    apistep = models.CharField('测试步骤', max_length=100, null=True)
    apiparamvalue = models.CharField('请求参数和值', max_length=800)
    REQUEST_METHOD = (('0', 'get'), ('1', 'post'), ('2', 'put'), ('3', 'delete'), ('4', 'patch'))
    apimethod = models.CharField(verbose_name='请求方法', choices=REQUEST_METHOD, default='get', max_length=200, null=True)
    apiresult = models.CharField('预期结果', max_length=200)
    apistep = models.CharField('测试步骤', max_length=100, null=True)
    apistatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间', auto_now=True)
    producter = models.CharField('产品负责人', max_length = 200, null = True)
    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一场景接口'

    def __str__(self):
        return self.apiname
