from django.db import models

# Create your models here.
class create(models.Model):
    username=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    date=models.DateField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username