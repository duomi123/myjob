from django.conf.urls import url

from carts import views
app_name='usercart'
urlpatterns = [
    url(r'^cart/$',views.mycart,name='usercart'),
    url(r'^add_(\d+)_(\d+)/$',views.add,name='useradd'),
]