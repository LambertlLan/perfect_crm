# __author: Lambert
# __date: 2017/11/3 11:59
from django.conf.urls import url
from student import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name="stu_index"),
]
