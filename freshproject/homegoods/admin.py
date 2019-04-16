from django.contrib import admin

# Register your models here.
from homegoods.models import TypeInfo, GoodsInfo


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']
class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id','gname','gpic','gprice','gunit','gclick','gsummary','gkucun','gcontent','gjudgement','goodsadv','goodstype','isDelete']
admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)