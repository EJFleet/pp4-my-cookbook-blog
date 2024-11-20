from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class TeamMember(models.Model):
    """
    Create profiles for team members
    """
    name = models.CharField(max_length=30)
    jobtitle = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    headshot = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def latest_recipe(self):
        return self.recipes.order_by('-posted_date').first()
