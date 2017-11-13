from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django import views
from king_admin import king_admin, utils
from django.forms.models import model_to_dict


# Create your views here.
class Index(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'king_admin/king_admin.html', {'table_list': king_admin.enable_class})


class Display_table_objs(views.View):
    def get(self, request, app_name, table_name):
        print(app_name, table_name)
        admin_class = king_admin.enable_class[app_name][table_name]
        object_list, filter_condtions = utils.table_filter(request, admin_class)
        object_list = utils.search_filter(request, admin_class, object_list)
        object_list = utils.table_order_by(request, object_list)
        paginator = Paginator(object_list, admin_class.list_per_page)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            query_sets = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            query_sets = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            query_sets = paginator.page(paginator.num_pages)
        return render(request, 'king_admin/table-objs.html',
                      {'admin_class': admin_class, 'filter_conditions': filter_condtions, 'query_sets': query_sets})


class Display_table_objs_change(views.View):
    def get(self, request, app_name, table_name, obj_id):
        admin_class = king_admin.enable_class[app_name][table_name]
        query_sets = admin_class.model.objects.filter(id=obj_id)[0]
        return render(request, 'king_admin/table-objs-change.html', {'query_set': model_to_dict(query_sets)})
