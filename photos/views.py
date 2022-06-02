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
  '''
  View function to display all images and their descriptions.
  '''
  images = Image.getImages()
  locations = Location.objects.all()
  categories = Category.objects.all()
  return render(request, 'gallery.html', {"images":images,"locations":locations, "categories":categories })

def search_results(request):
  '''
  View function to display the searched categories' images.
  '''
  locations = Location.objects.all()
  categories = Category.objects.all()
  
  if 'category' in request.GET and request.GET["category"]:
      search_term = request.GET.get("category")
      searched_Images = Image.searchByCategory(search_term)
      message = f"{search_term}"

      return render(request, 'search.html',{"message":message,"searchedImages": searched_Images, "categories":categories, "locations":locations})

  else:
      message = "You haven't searched for any category"
      return render(request, 'search.html',{"message":message, "categories":categories,"location":locations})
