from django.db import models
from product.models import Product
# Create your models here.

#bug列表
class Bug(models.Model):
    Product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    bugname = models.CharField('bug名称',max_length=64)
    bugdetail = models.CharField('详情',max_length=200)
    BUG_STATUS = (('激活','激活'),('已解决','已解决'),('已关闭','已关闭'))
    bugstatus = models.CharField(verbose_name='解决状态',choices=BUG_STATUS,default='激活',max_length=200,null=True)
    BUG_LEVEL = (('紧急','紧急'),('严重','严重'),('一般','一般'))
    buglevel = models.CharField(verbose_name='严重程度',choices=BUG_LEVEL,default='一般',max_length=200,null=True)
    bugcreater = models.CharField('创建人',max_length=200)
    bugassign = models.CharField('分配给',max_length=200)
    create_time = models.DateTimeField('创建时间',auto_now=True)
    class Meta:
        verbose_name = 'bug管理'
        verbose_name_plural = 'bug管理'

    def __str__(self):
        return self.bugname

