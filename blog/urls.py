from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.AddRecipe.as_view(), name='add_recipe'),
    path('delete/<slug:slug>/', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('recipe/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name="comment_edit"),
    path('recipe/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    ]