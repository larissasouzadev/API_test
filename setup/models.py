from django.db import models
from django.utils.timezone import now

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    social_nature = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=11, default='')
    revenues = models.FloatField(blank=True, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
        
    def __str__(self):
        return self.name
    # class category
class Category(models.Model):
    name = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.name
class Sales(models.Model): 
     client = models.ForeignKey(Client, on_delete=models.CASCADE, default='')
     category = models.ForeignKey(Category,  on_delete=models.CASCADE)
     id_sale = models.AutoField(primary_key=True)  
     product = models.CharField(max_length=50,default='' )
     supplier = models.CharField(max_length=100, default='')
     price_sale = models.FloatField(blank=False, default=0.00)
     created_at = models.DateTimeField(auto_now_add=True,null=True)
     updated_at = models.DateTimeField(auto_now=True)
     class Meta:
        verbose_name_plural:'Sales'
     def __str__(self):
         return self.product
     