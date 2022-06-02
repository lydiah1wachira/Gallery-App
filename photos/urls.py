from django.urls import path,re_path
from . import views 

urlpatterrns = [
  path('index/', views.index, name='index' )
]