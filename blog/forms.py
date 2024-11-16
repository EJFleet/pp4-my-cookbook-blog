from .models import Comment, Recipe
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class RecipeForm(forms.ModelForm):
    ingredients = forms.CharField(widget=SummernoteWidget())
    method = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'servings',
                    'ingredients', 'method', 'featured_image',
                )
        
        labels = {
            'title': 'Recipe Title',
            'description': 'Recipe Description',
            'servings': 'Servings',
            'ingredients': 'Ingredients',
            'method': 'Instructions',
            'featured_image': 'Recipe Image',
        }