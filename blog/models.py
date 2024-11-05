from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    title = models.CharField(max_length=200, null=False, blank=False, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_writer")
    description = models.CharField(max_length=500, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)