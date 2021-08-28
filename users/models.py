from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image

from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    email = models.EmailField(max_length=150)
    signup_confirmation = models.BooleanField(default=False)

    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs) 
        img=Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)   

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()



class scrap(models.Model):
    text= models.CharField(max_length=255)
    upload = models.FileField(upload_to='upload/%Y/%m/%d/')    

# Create your models here.

class students(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email=models.EmailField(max_length=254)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("update", kwargs={"id": self.id})


