from django.conf.urls import url

from homegoods import views
app_name = 'homegoods'#这里的名字定义没有要求

urlpatterns = [

    url(r'^index/$',views.index,name='userindex'),
    url(r'^detail/(\d+)/$',views.detail,name='userdetail'),
    url(r'^list/(\d+)/(\d+)/(\d+)/$',views.list,name='userlist'),
    # url(r"^gcontentedit/$", views.gcontentedit,name='usertemp'),
    # url(r"^saveedit/$", views.saveedit,name='usertemp'),

]