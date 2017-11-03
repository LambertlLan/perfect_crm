# __author: Lambert
# __date: 2017/10/17 11:35
from django import template
from django.utils.safestring import mark_safe

register = template.Library()  # register的名字是固定的,不可改变


# 定义为tag，不能再if后面作为条件
@register.simple_tag
def render_table_name(obj):
    return obj.model._meta.verbose_name_plural


@register.simple_tag
def get_query_sets(admin_class):
    return admin_class.model.objects.all


@register.simple_tag
def build_table_row(item, title):
    field_obj = item._meta.get_field(title)
    # 获取choice对象，有则返回元组，没有返回空列表
    if field_obj.choices:
        return getattr(item, "get_%s_display" % title)()  # 此为一个方法，执行后返回数据
    else:
        return getattr(item, title)
