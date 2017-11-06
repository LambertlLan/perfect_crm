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
def get_field_obj(filt, admin_class):
    field_obj = admin_class.model._meta.get_field(filt)
    if field_obj.choices:
        return field_obj.choices
    if type(field_obj).__name__ == "ForeignKey":
        return field_obj.get_choices()


@register.simple_tag
def build_table_row(item, title):
    field_obj = item._meta.get_field(title)
    # 获取choice对象，有则返回元组，没有返回空列表
    if field_obj.choices:
        return getattr(item, "get_%s_display" % title)()  # 此为一个方法，执行后返回数据
    else:
        return getattr(item, title)


@register.simple_tag
def render_filter_eles(conditon, admin_class, filter_conditions):
    fidld_obj = admin_class[conditon]._meta.get_field(conditon)
    return getattr(admin_class[conditon], )


@register.simple_tag
def get_filter_conditions_condition(filter_conditions, condition):
    if condition in filter_conditions:
        return int(filter_conditions[condition])


@register.simple_tag
def get_current_page_str(urlencode, current_page, page):
    current_page_str = ''.join(('page=', str(current_page),))
    page_str = ''.join(('page=', str(page),))
    return '?' + urlencode.replace(current_page_str, page_str, 1)


@register.filter
def test(current_page_str, current, page):
    return current_page_str.replace(current_page_str, 'lesson', 1)
