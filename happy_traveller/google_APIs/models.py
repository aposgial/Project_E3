from django.db import models

# Create your models here.
class Place(models.Model):
    place_id = models.CharField(max_length=800)
    base_photo = models.ImageField(upload_to='static/photos', blank=True)


class PlacePhotos(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/photos', blank=True)
    