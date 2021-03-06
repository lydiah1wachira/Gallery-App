from django.urls import path,re_path
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('', views.index, name='index' ),
  path('gallery/', views.gallery, name='gallery'),
  path('search/', views.search_results, name='search_results'),
  path('location/<location_id>/', views.filterByLocation, name='location'),
  re_path(r'details/(\d+)',views.detailedImage,name ='detailedImage'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)