from django.db import models

from category.models import Category

# Create your models here.

class Task(models.Model):
    Title=models.CharField(max_length=50)
    TaskDescription=models.TextField()
    Date=models.DateField()
    catagory=models.ManyToManyField(Category)
    complete=models.BooleanField(default=False)



    def __str__(self):
      return self.Title