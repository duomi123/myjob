from django.db import models

# Create your models here.
#自定义模型管理器类中添加方法 创建对象
from tinymce.models import HTMLField


class Goods_Manager(models.Manager):#继承models.Manager
    def get_queryset(self):
        return super(Goods_Manager, self).get_queryset().filter(is_delete=False)  # 重写查询器 将数据库中逻辑删除的字段过滤不要

class Info_Manager(models.Manager):
    def get_queryset(self):
        return super(Info_Manager, self).get_queryset().filter(is_delete=False)  # 将数据库中逻辑删除的字段过滤不要

class TypeInfo(models.Model):
    typeobj = models.Manager()
    typesobj2 = Info_Manager()
    title= models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'typeinfo'

    def __str__(self):
        return self.title
class GoodsInfo(models.Model):
    # 当自定义模型管理器时，objects 就不存在了
    goodsobj = models.Manager()
    goodsobj2 = Goods_Manager()
    gname = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='userinfo/images/goods')
    gprice =models.DecimalField(max_digits=5,decimal_places=2)#整数5位数，小数部分2位数 999.99
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField()#点击量
    gsummary =models.CharField(max_length=200)
    gkucun = models.IntegerField()#简介
    gcontent = HTMLField()
    gjudgement=models.CharField(max_length=200)#评价
    isDelete =models.BooleanField(default=False)
    goodstype =models.ForeignKey(TypeInfo,on_delete=models.DO_NOTHING)
    goodsadv =models.BooleanField(default=False)#推荐商品 默认不推荐

    class Meta:
        db_table = 'goodsinfo'
    def __str__(self):
        return str(self.goodstype)




