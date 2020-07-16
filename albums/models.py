from django.db import models

# Create your models here.
class Album(models.Model):

    artistname = models.CharField(max_length=255, null = True, blank = True)
    albumtitle = models.CharField(max_length=255,null = True, blank = True)
    released = models.DateField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
   
    
    
    def __str__(self):
      return f"{self.albumtitle} by {self.artistname}"

class Users(models.Model):
  pass
  