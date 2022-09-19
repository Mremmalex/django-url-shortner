from django.db import models

# Create your models here.


class Url(models.Model):
    slug = models.CharField(max_length=400, unique=True)
    site = models.CharField(max_length=400)

    def __str__(self) -> str:
        return self.slug
