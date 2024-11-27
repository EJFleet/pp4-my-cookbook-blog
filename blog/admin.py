from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment
from .forms import RecipeAdminForm


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Recipe model.
    Includes support for Summernote fields.
    """
    form = RecipeAdminForm
    list_display = ('title', 'slug', 'status', 'posted_date')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    Provides filtering and search functionality.
    """
    list_display = ('recipe', 'author', 'body', 'created_on')
    list_filter = ('recipe', 'created_on')
    search_fields = ('body', 'author__username', 'recipe__title')
