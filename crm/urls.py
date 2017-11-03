# __author: Lambert
# __date: 2017/11/3 10:29
from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name="sales_index"),
    url(r'^customers/$', views.CustomerList.as_view(), name="customer_list")
]
