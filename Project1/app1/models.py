from django.db import models

# Create your models here.

class ImageData(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to="all_images")

    def __str__(self) -> str:
        return self.name