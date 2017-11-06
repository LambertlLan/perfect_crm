# __author: Lambert
# __date: 2017/11/3 15:31
from crm import models


class BaseAdmin(object):
    list_display = ()
    list_filter = []


class CustomerAdmin(BaseAdmin):
    list_display = ('id', 'qq', 'source', 'consultant','consult_course', 'date',)
    list_filters = ['source', 'consultant', 'consult_course']
    list_per_page = 1


enable_class = {}


def register(model_class, admin_class):
    if model_class._meta.app_label not in enable_class:
        enable_class[model_class._meta.app_label] = {}
    admin_class.model = model_class
    enable_class[model_class._meta.app_label][model_class._meta.model_name] = admin_class


register(models.Customer, CustomerAdmin)
