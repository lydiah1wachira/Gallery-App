from django.db import models
from django.forms import CharField

# Create your models here.
class Category(models.Model):
  '''
  Class to help create instances of different Photo category models."
  '''
  name = CharField(max_length=30)

  def __str__(self):
        return self.name

  def saveCategory(self):
      self.save()