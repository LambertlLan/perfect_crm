from django.shortcuts import render, HttpResponse
from django import views
from king_admin import king_admin


# Create your views here.
class Index(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, 'king_admin/king_admin.html', {'table_list': king_admin.enable_class})


class Display_table_objs(views.View):
    def get(self, request, app_name, table_name):
        print(app_name, table_name)
        admin_class = king_admin.enable_class[app_name][table_name]
        return render(request, 'king_admin/table-objs.html', {'admin_class': admin_class})
