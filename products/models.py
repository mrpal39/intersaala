from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
class Products(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    weight= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    price=  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock=  models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    create_at= models.DateField(auto_now=True)
    update_at= models.DateTimeField(auto_now_add=True)
    class  Meta:
        db_table = 'Products'
        managed = True
        ordering = ('-name',)

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
