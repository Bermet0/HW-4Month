from django.db import models


# Create your models here.
class LitresModel(models.Model):
    title_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title_name