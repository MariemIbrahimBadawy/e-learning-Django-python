from django.db import models

# Create your models here.

class Courses(models.Model):
    name    = models.CharField(max_length=150)
    discrip = models.CharField(max_length=1000)
    price   = models.DecimalField(max_digits=5 , decimal_places=3)

    def __str__(self):
        return self.name