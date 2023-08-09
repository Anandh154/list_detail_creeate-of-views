from django.shortcuts import render
from app.models import *
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.

class SchoolListView(ListView):
    model=School
    context_object_name="allso"
    #template_name="school_list.html"

class SchoolDetailView(DetailView):
    model=School
    context_object_name="DOSI"

class SchoolCreate(CreateView):
    model=School
    fields="__all__"
    
    