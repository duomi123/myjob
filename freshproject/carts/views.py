from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from carts.models import CartsInfo
from userinfo import user_decorate


@user_decorate.login
def mycart(request):
    uid = request.session['user_id']
    carts = CartsInfo.objects.filter(user_id=uid)
    context ={'title':'购物车','carts':carts}
    if  request.is_ajax() :#在首页 购物车可以看到数量
        count = CartsInfo.objects.filter(user_id=uid).count()#返回的是种类
        context = {'count':count}
        return JsonResponse(context)
    return render(request,'homegoods/cart.html',context)
@user_decorate.login
def add(request,gid,gcounts):
    uid = request.session['user_id']
    cart = CartsInfo.objects.filter(user_id=uid,goods_id=int(gid))
    if len(cart)>=1:#该商品在购物车中存在 只需增加数量  因为购物车当提交订单时 购物车已经清空，所以保证购物车该商品只有一种
        cart=cart[0]#只有一种所以取0
        cart.counts = cart.counts + int(gcounts)
    else:
        cart = CartsInfo()#没有  需要构建对象
        cart.goods_id = int(gid)
        cart.counts = int(gcounts)
        cart.user_id =uid
    cart.save()
    # count = CartsInfo.objects.filter(user_id=uid).count()#返回的是种类
    # context = {'count':count}
    # return JsonResponse(context)
    if  request.is_ajax() :#在详情页 添加购物车要返回数据
        count = CartsInfo.objects.filter(user_id=uid).count()#返回的是种类
        context = {'count':count}
        return JsonResponse(context)
    else:
        return redirect('/user/cart/') # 返回购物车