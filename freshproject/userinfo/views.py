from hashlib import sha1

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from userinfo.models import Userinfo



def register(request):

    return render(request, 'userinfo/registerbase.html')
def register_handle(request):

    user =Userinfo()
    user.name= request.POST.get('user_name')
    user.email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    ucpwd = request.POST['cpwd']
    # if Userinfo.objects.filter(name=user.name).count():
    #     return render(request, 'userinfo/registerbase.html', {'error_name': True})
    # if Userinfo.objects.filter(email=user.email).count():
    #     return render(request, 'userinfo/registerbase.html', {'error_email': True})
    if pwd == ucpwd :
        # 加密
        s1 = sha1()
        s1.update(pwd.encode("utf8"))
        pwd2 = s1.hexdigest()
        user.pwd = pwd2
        # print(pwd2)
        # print(len(pwd2))
        user.save()
        return redirect('/login/')
    else:
        return redirect('/register/')

def uname_exist(request):
    uname = request.GET.get('uname')
    count = Userinfo.objects.filter(name=uname).count()
    return JsonResponse({'count': count})
def uemail_exist(request):
    uemail = request.GET.get('uemail')
    count = Userinfo.objects.filter(email=uemail).count()
    return JsonResponse({'count': count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'uname': uname,'name_error': 0, 'pwd_error': 0}
    return render(request, 'userinfo/loginbase.html',context)
def login_handle(request):
    post= request.POST
    uname= post.get('username')
    upwd = post.get('pwd')
    checkuname = post.get('checkuname',0)#如果用户勾选 则可以得到value值  如果得不到则 默认为0
    # 根据用户名查对象  用get方法也可以 但是get方法如果差不多会报异常 需要try 做判定，而filter 查不到则为返回[] 空
    user = Userinfo.objects.filter(name=uname)
    if len(user)==1:
        s1 = sha1()
        s1.update(upwd.encode("utf8"))
        upwd2 = s1.hexdigest()
        if user[0].pwd == upwd2:
            red =HttpResponseRedirect('/user_info/')# 这里不能用redirect 因为要设置cookie值 redirect继承 HttpResponseRedirect
            if checkuname !=0 :
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)#-1是关闭就会清cookie
            request.session['user_name']=uname
            request.session['user_id'] = user[0].id
            return red

        else:
            context={'uname':uname,'upwd':upwd,'name_error':0,'pwd_error':1}#用户名对 密码错
            return render(request, 'userinfo/loginbase.html', context)

    else:
        context={'uname':uname,'upwd':upwd,'name_error':1,'pwd_error':0}#用户名错 密码不关心
        return render(request,'userinfo/loginbase.html',context)


def user_info(request):
    uname = request.session.get('user_name')
    user = Userinfo.objects.filter(name=uname).first()
    # print(user)
    return render(request, 'userinfo/user_center_info.html',{'user':user,'uname':uname})
def user_center_order(request):
    uname = request.session.get('user_name')
    return render(request, 'userinfo/user_center_order.html',{'uname':uname})
def user_center_site(request):
    uname = request.session.get('user_name')
    user = Userinfo.objects.filter(name=uname).first()
    return render(request, 'userinfo/user_center_site.html',{'user':user,'uname':uname})
def user_center_site_handle(request):

    uid =request.session.get('user_id')
    user = Userinfo.objects.get(id=uid)
    # if request.method =='POST':#这里表单提交时用post 方法
    post = request.POST
    user.receiver = post.get('receiver')
    user.address = post.get('addr')
    user.postcode = post.get('postcode')
    user.telephone = post.get('telephone')
    user.save()
    return  redirect('/user_center_site/')
def place_order(request):
    return render(request,'userinfo/place_order.html')
