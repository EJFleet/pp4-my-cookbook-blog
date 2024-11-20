from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class TeamMember(models.Model):
    """
    Create profiles for team members
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    bio = models.TextField(max_length=1000, null=False, blank=False, default="A wonderul team member!")
    jobtitle = models.CharField(max_length=50, verbose_name='Job Title')
    location = models.CharField(max_length=60)
    headshot = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name