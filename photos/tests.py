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



