from django.db import models

# Create your models here.
class Review(models.Model):
    user_name=models.CharField(max_length=50)
    rating=models.IntegerField()
    review_text=models.TextField()