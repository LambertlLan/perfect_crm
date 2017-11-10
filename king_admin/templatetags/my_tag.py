# __author: Lambert
# __date: 2017/10/17 11:35
from django import template
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime, timedelta

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
    # 返回choices
    if field_obj.choices:
        # return field_obj.choices 第一个返回-----------
        return field_obj.get_choices()
    # 返回ForeignKey
    if type(field_obj).__name__ == "ForeignKey":
        return field_obj.get_choices()
    # 返回日期类型
    if type(field_obj).__name__ in ['DateTimeField', 'DateField']:
        date_els = []
        today_ele = datetime.now().date()
        date_els.append(["", '---------------', ])
        date_els.append([datetime.now().date().strftime("%Y-%m-%d"), '今天', ])
        date_els.append([(today_ele - timedelta(days=1)).strftime("%Y-%m-%d"), "昨天", ])
        date_els.append([(today_ele - timedelta(days=7)).strftime("%Y-%m-%d"), "近7天", ])
        date_els.append([(today_ele.replace(day=1)).strftime("%Y-%m-%d"), "本月", ])
        date_els.append([(today_ele - timedelta(days=30)).strftime("%Y-%m-%d"), "近30天", ])
        date_els.append([(today_ele - timedelta(days=90)).strftime("%Y-%m-%d"), "近90天", ])
        date_els.append([(today_ele - timedelta(days=180)).strftime("%Y-%m-%d"), "近180天", ])
        date_els.append([(today_ele.replace(month=1, day=1)).strftime("%Y-%m-%d"), "本年", ])
        date_els.append([(today_ele - timedelta(days=365)).strftime("%Y-%m-%d"), "近一年", ])
        return date_els


@register.simple_tag
def build_table_row(item, title):
    field_obj = item._meta.get_field(title)
    # 获取choice对象，有则返回元组，没有返回空列表
    if field_obj.choices:
        return getattr(item, "get_%s_display" % title)()  # 此为一个方法，执行后返回数据
    else:
        value = getattr(item, title)
        if type(value).__name__ == 'datetime':
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return value


@register.simple_tag
def render_filter_eles(conditon, admin_class, filter_conditions):
    fidld_obj = admin_class[conditon]._meta.get_field(conditon)
    return getattr(admin_class[conditon], )


@register.simple_tag
def get_filter_conditions_condition(filter_conditions, condition):
    if condition == 'date' and 'date__gte' in filter_conditions:
        return filter_conditions['date__gte']
    if condition in filter_conditions:
        return int(filter_conditions[condition])


@register.simple_tag
def get_current_page_str(urlencode, current_page, page):
    current_page_str = ''.join(('page=', str(current_page),))
    page_str = ''.join(('page=', str(page),))
    if urlencode:
        if urlencode.find(current_page_str) == -1:
            return ''.join(('?', urlencode, '&', page_str,))
        else:
            return ''.join(('?', urlencode.replace(current_page_str, page_str, 1),))
    else:
        return ''.join(('?', page_str))


@register.simple_tag
def order_by_filter(thead, o, urlencode):
    o_str = ''.join(('o=', o,))
    if o:
        if thead == o:
            return ''.join(('?', urlencode.replace(o_str, 'o=-%s' % thead, 1),))
        else:
            return ''.join(('?', urlencode.replace(o_str, 'o=%s' % thead, 1),))
    else:
        return ''.join(('?', urlencode, '&o=', thead,))


@register.filter
def judge_date(condition):
    if condition == 'date':
        return 'date__gte'
    else:
        return condition
