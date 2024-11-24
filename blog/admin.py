from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment
from .forms import RecipeAdminForm
@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    form = RecipeAdminForm

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'method',)

# Register your models here.
admin.site.register(Comment)