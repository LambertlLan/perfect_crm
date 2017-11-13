# __author: Lambert
# __date: 2017/11/3 15:21
from django.conf.urls import url
from king_admin import views

urlpatterns = [
    url(r'^$', views.Index.as_view()),
    url(r'^(\w+)/(\w+)/$', views.Display_table_objs.as_view(), name="table_objs"),
    url(r'^(\w+)/(\w+)/(\d+)/change/$', views.Display_table_objs_change.as_view(), name="table_objs_change"),
]
