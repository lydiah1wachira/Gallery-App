from django.shortcuts import render
from django.http import Http404
from .models import Image,Category,Location


# Create your views here.
def index(request):
  '''
  View function to Display the index page and its data."
  '''
  images = Image.getImages()
  locations = Location.objects.all()
  categories = Category.objects.all()

  return render(request, 'index.html', {"images":images,"locations":locations,"categories":categories})

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
  images = Image.getImages()
  locations = Location.objects.all()
  categories = Category.objects.all()
  
  if 'category' in request.GET and request.GET["category"]:
      search_term = request.GET.get("category")
      searched_Images = Image.searchByCategory(search_term)
      message = f"{search_term}"

      return render(request, 'search.html',{"message":message,"searchedImages": searched_Images, "categories":categories, "locations":locations, "images":images})

  else:
      message = "You haven't searched for any category"
      return render(request, 'search.html',{"message":message, "categories":categories,"location":locations})


def filterByLocation(request, location_id):
  '''
  View function to filter images based on their locations.
  '''
  locations = Location.objects.all()
  images = Image.getImages()
  categories = Category.objects.all()
  
  try:
      showlocations =Image.filterByLocation(location_id)

  except Image.DoesNotExist:
      raise Http404()
  return render(request,'location.html', { "locations": locations,"showlocations": showlocations,"images":images,"categories":categories}) 

def detailedImage(request, image_id):
  '''
  View function to display a larger image and its details.
  '''
  locations = Location.objects.all()
  try:
      image = Image.objects.get(id = image_id)
  except:
      raise Http404()
  return render(request, 'detailed-image.html', {'image':image,"locations":locations})

