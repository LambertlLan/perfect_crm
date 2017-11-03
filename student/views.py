from django.shortcuts import render
from crm import models
from django import views


# Create your views here.
class Index(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
