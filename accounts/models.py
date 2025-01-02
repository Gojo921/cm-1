from django.db import models
from django.contrib.auth.models import User

# Customer model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200,blank=True, null=True)
    last_name = models.CharField(max_length=200,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Customers(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
  

    def __str__(self):
        return self.name
    
# Product model
class Product(models.Model):
    CATEGORY = (
        ('indoor', 'Indoor'),
        ('outdoor', 'Outdoor'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
    


# Order model
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered'),
    )
    customer = models.ForeignKey(Customers, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)  # Corrected this line
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    

    def __str__(self):
        return f"Order by {self.customer.name} for {self.product.name}"
