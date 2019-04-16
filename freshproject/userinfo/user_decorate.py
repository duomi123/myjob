from django.http import HttpResponseRedirect


def login(func):
    def login_func(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            print('has session')
            return func(request,*args,**kwargs)
        else:#没有登陆则调到登陆页面
            red = HttpResponseRedirect('/login/')
            red.set_cookie('url',request.get_full_path())#保存客户进入时的路径登陆成功后，还返回以前的地方  从哪来到哪里去
            print('no has session')
            return red
    return  login_func

'''
http://127.0.01:8000/200/?page=20
request.path 返回的是当前路径  为 /200/  
request.get_full_path() 返回的是完成路径 为/200/?page=20 
'''
