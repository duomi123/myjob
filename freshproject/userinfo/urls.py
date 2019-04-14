from django.conf.urls import url

from userinfo import views
urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^uname_exist/$', views.uname_exist),
    url(r'^uemail_exist/$', views.uemail_exist),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^user_info/$', views.user_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^user_center_site_handle/$', views.user_center_site_handle),
    url(r'^place_order/$', views.place_order),

]