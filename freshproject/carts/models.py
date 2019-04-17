from django.db import models

# Create your models here.
class CartsInfo(models.Model):
    counts = models.IntegerField()
    user   = models.ForeignKey('userinfo.Userinfo',on_delete=models.DO_NOTHING)
    goods  = models.ForeignKey('homegoods.GoodsInfo',on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'cartsinfo'
