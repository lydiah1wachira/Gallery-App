from django.urls import path,re_path
from . import views 

urlpatterrns = [
  path('', views.index, name='index' )
]