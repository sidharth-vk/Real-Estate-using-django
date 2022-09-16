from django.db import models
from django.db.models.signals import  post_save
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    

class Listing(models.Model):
    title = models.CharField( max_length=150)
    price = models.IntegerField()
    discription = models.CharField( max_length=50)
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField( max_length=150)
    image = models.ImageField( )
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)
    
    
def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal,sender=User)