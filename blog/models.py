from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # from CI
from team.models import TeamMember

STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    """
    A model to create and manage recipes
    """
    title = models.CharField(
        max_length=200, null=False, blank=False, unique=True
        )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        TeamMember, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='recipes'
        )
    description = models.CharField(max_length=500, null=False, blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    servings = models.IntegerField(
        null=False, blank=False, default=4,
        help_text='Enter how many people your recipes serves.'
        )
    ingredients = models.TextField(
        max_length=10000, null=False, blank=False, default='Ingredients needed'
        )
    method = models.TextField(
        max_length=10000, null=False, blank=False, default='Method needed'
        )
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return str(self.title)


class Comment(models.Model):

    """
    Allow users to create and manage comments
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_comments"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
        )
    body = models.TextField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
