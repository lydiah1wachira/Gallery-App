from django.db import models


# Create your models here.
class Category(models.Model):
  '''
  Class to help create instances of different Photo category models."
  '''
  name = models.CharField(max_length=30)

  def __str__(self):
        return self.name

  def saveCategory(self):
      self.save()


class Location(models.Model):
  '''
  class to help create new instances of location object
  '''

  name = models.CharField(max_length=30)

  def __str__(self):
      return self.name
      
  def saveLocation(self):
      self.save()

class Image(models.Model):
  '''
  Image model to help create new instances of an image object
  '''
  name = models.CharField(max_length=30)
  description = models.TextField()
  photo = models.ImageField(upload_to = 'gallery_images/', null=True, blank=True)
  pub_date = models.DateTimeField(auto_now_add=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

  def __str__(self):
      return self.description

  def save_image(self):
      self.save()

  def delete_image(self):
      self.delete()

  def updateImage(self):
    self.update()