from django.db.models import Q
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic import CreateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import (UserPassesTestMixin, LoginRequiredMixin)
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


def get_recipe_queryset(user):
    """
    Return a queryset for recipes visible to the given user.
    """
    if user.is_authenticated:
        # Include published recipes and drafts authored by the user
        return Recipe.objects.filter(Q(status=1) | Q(author=user))
    else:
        # Include only published recipes for unauthenticated users
        return Recipe.objects.filter(status=1)

class RecipeList(generic.ListView):
    template_name = 'blog/index.html'
    paginate_by = 6

    def get_queryset(self):
        return get_recipe_queryset(self.request.user)


def recipe_detail(request, slug):
    """
    Display an individual :model:`blog.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    """

    queryset = get_recipe_queryset(request.user)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.recipe_comments.all().order_by("-created_on")
    comment_count = recipe.recipe_comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/recipe_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form" : comment_form,
        },
    )


class AddRecipe(CreateView):
    """ Add recipe view """
    template_name = "blog/add_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        # Automatically generate a unique slug for the recipe
        form.instance.author = self.request.user
        # Determine if the recipe is a draft or published based on the button clicked
        if self.request.POST.get('action') == 'draft':
            form.instance.status = 0  # Draft
        else:
            form.instance.status = 1  # Published

        if not form.instance.slug:
            form.instance.slug = slugify(form.instance.title)
        
        return super(AddRecipe, self).form_valid(form)

    def get_success_url(self):
        # Redirect to the detail page of the newly created recipe if status is 'published'
        if self.object.status == 1:
            return reverse('recipe_detail', kwargs={'slug': self.object.slug})
        else: # draft
            return reverse('home') #redirect to the recipe list

class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ Delete a recipe """

    model = Recipe
    template_name = "blog/recipe_confirm_delete.html"
    success_url = '/'

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))
    

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))