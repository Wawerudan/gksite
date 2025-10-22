from django.db import models

# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name =models.CharField(max_length=200)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color=models.CharField(max_length=10,null=True,blank=True)
    size=models.CharField(max_length=10,null=True,blank=True)
    def __str__(self):
     return self.name
 

    
