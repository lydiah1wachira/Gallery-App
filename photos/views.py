from django.shortcuts import render
from django.http import Http404
from .models import Image,Category,Location


# Create your views here.
def index(request):
  '''
  View function to Display the index page and its data."
  '''
  return render(request, 'index.html')

def gallery(request):
  images = Image.getImages()
  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request, 'gallery.html', {"images":images,"locations":locations, "categories":categories })

