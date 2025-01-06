from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.IntegerField()
    def __str__(self):
        return f'name:{self.first_name} lastname{self.last_name} email{self.email} contact {self.contact}'