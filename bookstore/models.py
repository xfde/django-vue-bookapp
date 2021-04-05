from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Book(models.Model):
    author = models.TextField()
    title = models.TextField()
    description = models.TextField()
    poster_image = models.ImageField(blank=True,null=True,
        upload_to="covers/%Y/%m/%D/")

    def __str__(self):
        return f"author:{self.author},title:{self.title},description:{self.description},poster_image:{self.poster_image}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()