from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    def __str__(self):
      return f'name:{self.first_name} age{self.age}'
class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField()
    is_bestselling=models.BooleanField()
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    def __str__(self):
        return f'Title{self.title} Rating:{self.rating}'