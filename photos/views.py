from django.shortcuts import render
from django.http import Http404

# Create your views here.
def index(request):
  '''
  View function to Display the index page and its data."
  '''
  return render(request, 'index.html')