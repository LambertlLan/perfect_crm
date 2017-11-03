from django.shortcuts import render, HttpResponse, redirect
from crm import models
from django import views


# Create your views here.


class Index(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "sales.html")


class CustomerList(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "customers/customer_list.html")
