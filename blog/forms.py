from django import forms
from django_summernote.widgets import SummernoteWidget
from django.contrib.auth.models import User
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments.
    Connects to the Comment model.
    """
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    """
    Form for creating and editing recipes.
    Uses Summernote widget for the 'ingredients' and 'method' fields.
    """
    ingredients = forms.CharField(widget=SummernoteWidget())
    method = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'servings',
                  'ingredients', 'method', 'featured_image')
        
        labels = {
            'title': 'Recipe Title',
            'description': 'Recipe Description',
            'servings': 'Servings',
            'ingredients': 'Ingredients',
            'method': 'Instructions',
            'featured_image': 'Recipe Image',
        }


class RecipeAdminForm(forms.ModelForm):
    """
    Admin form for Recipe model.
    Filters the 'author' field to only include staff users.
    """
    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Initialize the RecipeAdminForm.
        Filters the 'author' queryset to include only staff users.
        """
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.filter(is_staff=True)
