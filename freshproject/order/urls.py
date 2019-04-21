from django.conf.urls import url

from order import views
app_name='userorder'
urlpatterns = [
    url(r'^order/$',views.myorder,name='userorder'),
    url(r'^handle_order/$',views.handle_order,name='uhandle_order'),
    # url(r'^edit_(\d+)_(\d+)/$',views.edit,name='useredit'),
    # url(r'^delete_(\d+)/$',views.delete,name='userdelete'),
]