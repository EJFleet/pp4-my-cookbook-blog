from django.core.validators import MaxLengthValidator
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # from CI
from team.models import TeamMember

STATUS = (
    (0, "Draft"),
    (1, "Published"),
)


class Recipe(models.Model):
    """
    A model to create and manage recipes.

    Fields:
        - title: A short, unique title for the recipe.
        - slug: A unique slug for the recipe, used in URLs.
        - author: A foreign key linking the recipe to the User who created it.
        - description: A brief description of the recipe, validated for a maximum length of 500 characters.
        - posted_date: The date and time the recipe was initially created.
        - status: An integer field indicating whether the recipe is in Draft (0) or Published (1) state.
        - servings: The number of servings the recipe yields.
        - ingredients: Detailed list of ingredients, saved as plain text.
        - method: Step-by-step instructions for the recipe, saved as plain text.
        - featured_image: An optional image for the recipe, stored in Cloudinary.

    Meta:
        - Orders recipes by `-posted_date` (most recent first).
    """
    title = models.CharField(
        max_length=55, null=False, blank=False, unique=True
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_writer"
    )
    description = models.TextField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(500)]
    )
    posted_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    servings = models.IntegerField(
        null=False, blank=False, default=4,
        help_text='Enter how many people your recipe serves.'
    )
    ingredients = models.TextField(
        null=False, blank=False, default='Ingredients needed'
    )
    method = models.TextField(
        null=False, blank=False, default='Method needed'
    )
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        """
        Return the string representation of a Recipe instance,
        which is its title.
        """
        return str(self.title)


class Comment(models.Model):
    """
    Allow users to create and manage comments on recipes.

    Fields:
        - recipe: A foreign key linking the comment to a specific recipe.
        - author: A foreign key linking the comment to the User who created it.
        - body: The main content of the comment, limited to 3000 characters.
        - created_on: The date and time the comment was created.
        - approved: A boolean indicating whether the comment has been approved by an admin.

    Meta:
        - Orders comments by `-created_on` (most recent first).
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
        """
        Return a string representation of a Comment instance,
        displaying the associated recipe, comment body, author, 
        and creation date.
        """
        return f"{self.recipe}: {self.body} by {self.author} | {self.created_on}"
