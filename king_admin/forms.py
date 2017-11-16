# __author: Lambert
# __date: 2017/11/16 23:16
from django.forms import forms, ModelForm

from crm import models


def creat_model_form(request, admin_class):
    """动态生成modelForm"""

    class Meta:
        model = admin_class.model
        fields = "__all__"

    attrs = {'Meta': Meta}
    _model_form_class = type("DynamicModelForm", (ModelForm,), attrs)

    return _model_form_class
