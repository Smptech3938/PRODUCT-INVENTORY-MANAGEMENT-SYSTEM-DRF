from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

class ProductModel(models.Model):
    CATEGORY_CHOICES=(
        ('electronics','electronics'),
        ('food','food'),
        ('cloths','cloths')
    )

    name=models.CharField(max_length=20)
    description=models.TextField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=25,choices=CATEGORY_CHOICES)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)