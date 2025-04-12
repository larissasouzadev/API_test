from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_lenght=50, default='')
    social_nature = models.CharField(max_leght=100, default='')
    phone = models.CharField(max_lenght=11, default='')
    revenues = models.FloatField(max_digits = 8, default=0.00)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    # class category
class Category(models.Model):
    name = models.CharField(max_leght=100, default='')
    def __str__(self):
        return self.name
class Sales(models.Model): 
     category = models.ForeignKey(Category,  on_delete=models.CASCADE)
     id_sale = models.AutoField(primary_key=True)  
     product = models.CharField(max_lenght=50,default='' )
     supplier = models.CharField(max_lenght=100, default='')
     price_sale = models.FloatField(max_digits=8, default=0.00)
     data = models.DateTimeField(auto_now=True)
     def __str__(self):
         return self.product