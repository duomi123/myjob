from django.core.paginator import Paginator
from django.http import response
from django.shortcuts import render

# Create your views here.
from homegoods.models import TypeInfo, GoodsInfo


def index(request):
    #查询各分类的最新4条 、点击量最高的4条数据
    typelist = TypeInfo.typeobj.all()
    type0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]
    context={'title':'首页',
             'type0':type0,'type01':type01,'type1':type1,
             'type11':type11,'type2':type2,'type21':type21,
             'type3': type3, 'type31': type31, 'type4': type4,
             'type41': type41, 'type5': type5, 'type51': type51,
             }
    return render(request,'homegoods/index.html',context)

def list(request,uid=1,numpage=1,sort=1):

    typelist = TypeInfo.typeobj.get(pk=int(uid))
    goodstype=typelist.title
    goods_news=typelist.goodsinfo_set.order_by('-id')[0:2]#新品推荐
    if sort=='1':#默认是新品排序
        goodslist=typelist.goodsinfo_set.order_by('-id')
    if sort=='2':#人气
        goodslist=typelist.goodsinfo_set.order_by('-gclick')
    if sort== '3':#价格
        goodslist = typelist.goodsinfo_set.order_by('gprice')
    paginator = Paginator(goodslist,10)#每一页10条数据
    page =paginator.page(int(numpage))

    context={'title':'商品列表',
             'goodstype':goodstype,'goods_news':goods_news,
             'uid':uid,'page':page,"sort":sort,'paginator':paginator}
    return render(request,'homegoods/list.html',context)

def detail(request,gid=1):

    gdatail = GoodsInfo.goodsobj.get(id=int(gid))
    gdatail.gclick=gdatail.gclick+1#维护一个点击量
    gdatail.save()
    gtype = TypeInfo.typeobj.get(pk=gdatail.goodstype_id)
    goods_news = GoodsInfo.goodsobj.filter(goodstype_id=gdatail.goodstype_id).order_by('-id')[0:2]  # 新品推荐
    context = {'title': '商品详情',
               'gtype': gtype, 'goods_news': goods_news,'gdatail': gdatail}
    response = render(request, 'homegoods/detail.html', context)

    #维护用户对商品的浏览记录
    # goodsid = '%d'%gid#把整数变为字符串
    goodsid=gid
    goodsids = request.COOKIES.get('goodsids','')
    if goodsids != '':                    #判断是否有浏览记录
        goodsid_list = goodsids.split(',')#将字符串以'，'拆分为列表
        if  goodsid_list.count(goodsid)>=1:#该商品已经在最近浏览列表里 则删除
            goodsid_list.remove(goodsid)
        goodsid_list.insert(0,goodsid) #添加到第一个
        if len(goodsid_list)>=6: #判断商品是否已经多于六个  多了则删除最后一个
            del goodsid_list[5]
        goodsids=','.join(goodsid_list) #将列表值拼接为字符串
    else:
        goodsids = goodsid#没有则直接添加
    response.set_cookie('goodsids',goodsids) #写入cookie
    return response

