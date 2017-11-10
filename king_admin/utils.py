# __author:  Administrator
# date:  2017/1/5
from django.db.models import Q


def table_filter(request, admin_class):
    """进行条件过滤并返回过滤后的数据"""
    filter_conditions = {}
    keywords = ['page', 'o', 'q']
    for k, v in request.GET.items():
        if k in keywords:
            continue
        if v:
            if k == 'date':
                filter_conditions['date__gte'] = v
            else:
                filter_conditions[k] = v
    return admin_class.model.objects.filter(**filter_conditions), filter_conditions


def table_order_by(request, object_list):
    order_key = request.GET.get('o')
    if order_key:
        return object_list.order_by(order_key)
    else:
        # 设置默认以id排序
        return object_list.order_by('id')


def search_filter(requset, admin_class, object_list):
    search_key = requset.GET.get('q')
    if search_key:
        q_obj = Q()
        q_obj.connector = "OR"
        for field in admin_class.search_fields:
            q_obj.children.append(('%s__contains' % field, search_key))
        return object_list.filter(q_obj)
    else:
        return object_list
