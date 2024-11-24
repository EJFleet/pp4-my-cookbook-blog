from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe
from django.contrib.auth.models import User


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


class RecipeAdminForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter the author field to only include staff users
        self.fields['author'].queryset = User.objects.filter(is_staff=True)