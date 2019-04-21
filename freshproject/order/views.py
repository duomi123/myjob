from datetime import datetime

import simplejson as simplejson
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from carts.models import CartsInfo
from homegoods.models import GoodsInfo
from order.models import OrderProduct, OrderInfo
from userinfo import user_decorate
from userinfo.models import Userinfo


# @user_decorate.login
# def myorder(request):
#
#     uid = request.session.get('user_id', '')
#     user = Userinfo.objects.get(id=uid)
#     id_list =request.POST.get('listid')
#     list_ids = simplejson.loads(id_list)#simplejson 需要安装 simplejson的loads方法将其转换为字典数据类型
#                                      # simplejson的dumps方法, 将字典数据dict序列化为字符串形式,将通过HttpResponse返回.
#
#     cart=[]
#     for list_id in list_ids:
#         cart.append(CartsInfo.objects.get(id=int(list_id)))
#     context = {'title':'提交订单','user':user,'cart':cart}
#     # if request.is_ajax():
#     #     context = {'count': 0}
#     #     return JsonResponse(context)
#
#     return render(request, 'userinfo/place_order.html',context)

# 生成订单
@user_decorate.login
def myorder(request):
    if request.method == 'POST':
        uid = request.session.get('user_id', '')
        user = Userinfo.objects.get(id=uid)
        sku_ids = request.POST.getlist('sku_id', '')
        # print(sku_ids)
        carts = []
        if sku_ids == '':
            return redirect(reverse('carts:usercart'))  # 返回购物车
        else:
            for sku_id in sku_ids:
                carts.append(CartsInfo.objects.get(id=int(sku_id)))
        context = {'title': '提交订单', 'user': user, 'carts': carts,'sku_ids':sku_ids}
        # print(type(carts))
        # print('*****************')
        return render(request, 'userinfo/place_order.html', context)
    return redirect(reverse('carts:usercart'))


'''
事务处理：一旦操作失败全部回退
1,创建订单对象
2，判断商品的库存
3，创建详单
4，修改商品库存
5，删除购物车信息
'''


# 提交订单并处理
@transaction.atomic  # 装饰器事务
@user_decorate.login
def handle_order(request):
    if request.method == 'POST':
        uid = request.session.get('user_id', '')
        user = Userinfo.objects.get(id=uid)
        addr = request.POST.get('address')
        pay_id = request.POST.get('pay_id')
        skus = request.POST.get('skus')
        address = addr.split(',')

        if len(address) < 3:
            return JsonResponse({'res': 0, 'msg': '地址不完整'})
        addr = ''.join(address)
        # print(addr)
        print(skus)
        if not all([addr, pay_id, skus]):
            return JsonResponse({'res': 3, 'msg': '数据不完整'})
        # 想订单信息表中添加记录
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(uid)
        transition = 10
        total_count = 0
        total_price = 0
        # 设置事务保存点
        tran_id = transaction.savepoint()
        try:
            # orderproduct = OrderProduct()  # 创建订单对象
            order = OrderInfo.objects.create(order_id=order_id, pay_method=pay_id, transit_price=transition,
                                             user=user, addr=addr, product_count=total_count, product_price=total_price)
            # 想订单商品表中添加数据
            for sku in eval(skus):#eval 将字符串转为列表或者字典 元组
                # print(sku)
                # print(type(sku))
                cart = CartsInfo.objects.get(id=int(sku))
                if int(cart.counts) > cart.goods.gkucun:
                    transaction.savepoint_rollback(tran_id)
                    return JsonResponse({'res': 6, 'msg': '库存不足'})

                OrderProduct.objects.create(order_info=order, product=cart.goods, price=cart.goods.gprice,
                                                   count=cart.counts)

                # 更新销量、库存
                cart.goods.gkucun -= int(cart.counts)

                cart.goods.save()

                # 累加总金额、总数量

                total_price += cart.goods.gprice * int(cart.counts)

                total_count += int(cart.counts)
                # 删掉购物车数据
                cart.delete()

            # 更新订单信息表中的数据

            order.product_count = total_count

            order.product_price = total_price

            order.save()

            transaction.savepoint_commit(tran_id)
        except Exception as ex:
            print(ex)
            transaction.savepoint_rollback(tran_id)
            return JsonResponse({'res': 7, 'msg': '下单失败'})

            # 下订单后清除购物车数据

        return JsonResponse({'res': 5, 'msg': '创建成功'})


@user_decorate.login
def pay_order(request):
    pass
