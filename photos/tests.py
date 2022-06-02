from django.test import TestCase
from .models import Category, Location, Image

# Create your tests here.

class CategoryTestclass(TestCase):

  def setUp(self):
    self.art = Category(name = 'art')

  def test_instance(self):
    self.assertTrue(isinstance(self.art,Category))

  def test_save_method(self):
    self.art.saveCategory()
    categories = Category.objects.all()
    self.assertTrue(len(categories) > 0)

class LocationTestclass(TestCase):
  def setUp(self):
    self.nairobi = Location(name = 'nairobi')

  def test_instance(self):
    self.assertTrue(isinstance(self.nairobi,Location))

  def test_save_method(self):
    self.nairobi.saveLocation()
    locations = Location.objects.all()
    self.assertTrue(len(locations) > 0)

  


