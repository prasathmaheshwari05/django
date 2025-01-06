from django.db import models

# Create your models here.
class Chef(models.Model):
    full_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    age=models.IntegerField()

    def __str__(self):
      return f'name:{self.full_name} age{self.age} our address{self.address}'

class Dishes(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    is_billing=models.IntegerField()
    price=models.IntegerField()
    Demo=models.ForeignKey('Chef',on_delete=models.CASCADE)
    def __str__(self):
        return f'Title{self.name} Rating:{self.rating} is billing{self.is_billing} price is{self.price}'