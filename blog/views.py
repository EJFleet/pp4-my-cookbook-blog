from allauth.account.views import LoginView, LogoutView, SignupView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


def get_recipe_queryset(user):
    """
    Return a queryset for recipes visible to the given user.

    Authenticated users see published recipes and their own draft recipes.
    Unauthenticated users only see published recipes.
    """
    if user.is_authenticated:
        # Include published recipes and drafts authored by the user
        return Recipe.objects.filter(Q(status=1) | Q(author=user))
    else:
        # Include only published recipes for unauthenticated users
        return Recipe.objects.filter(status=1)


class RecipeList(generic.ListView):
    """
    Display a list of recipes.

    This view also supports filtering recipes based on a user's search query
    and pagination for better usability.
    """
    model = Recipe
    template_name = 'blog/index.html'
    paginate_by = 8

    def get_queryset(self):
        """
        Get the list of recipes to display.

        Incorporates user-specific filtering and search functionality.
        """
        query = self.request.GET.get('q')

        if self.request.user.is_staff:
            recipes = Recipe.objects.all()
        else:
            recipes = Recipe.objects.filter(status=1)

        if query:
            # Filter recipes by matching the search query to various fields
            recipes = recipes.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(method__icontains=query)
            )

        return recipes

    def get_context_data(self, **kwargs):
        """
        Add additional context data to the view.

        Includes the search query and dynamic page title based on the search.
        """
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        context['page_title'] = f"Search Results for '{query}'" if query else "Recipes"

        return context


def recipe_detail(request, slug):
    """
 Display an individual :model:`blog.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`blog.Recipe`.

    **Template:**

    :template:`blog/recipe_detail.html`
    
    Args:
        request: The HTTP request object.
        slug: The slug of the recipe.

    Returns:
        Rendered HTML for the recipe details page.
    """
    if request.user.is_staff:
        queryset = Recipe.objects.all()
    else:
        queryset = Recipe.objects.filter(status=1)

    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.recipe_comments.all().order_by("-created_on")
    comment_count = recipe.recipe_comments.filter(approved=True).count()

    if request.method == "POST":
        # Handle comment submission
        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create and save the new comment
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

            return redirect('recipe_detail', slug=recipe.slug)

    comment_form = CommentForm()
    page_title = recipe.title

    return render(
        request,
        "blog/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "page_title": page_title,
        },
    )


class AddRecipe(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    View for staff members to add a new recipe.
    """
    template_name = "blog/add_recipe.html"
    model = Recipe
    form_class = RecipeForm

    def test_func(self):
        """
        Restrict access to staff members only.
        """
        return self.request.user.is_staff

    def form_valid(self, form):
        """
        Save the form data for a new recipe.

        Assigns the logged-in user as the author and determines whether the 
        recipe is saved as a draft or published.
        """
        form.instance.author = self.request.user
        form.instance.status = 0 if self.request.POST.get('action') == 'draft' else 1

        if not form.instance.slug:
            # Generate a unique slug if one is not provided
            form.instance.slug = slugify(form.instance.title)

        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the appropriate page after the recipe is saved.

        Draft recipes redirect to the home page, and published recipes redirect
        to their detail page.
        """
        if self.object.status == 1:
            return reverse('recipe_detail', kwargs={'slug': self.object.slug})
        return reverse('home')

    def get_context_data(self, **kwargs):
        """
        Add additional context to the recipe creation view.

        Includes a page title for better user experience.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Recipe'
        return context


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for staff members to edit an existing recipe.
    """
    template_name = 'blog/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm

    def test_func(self):
        """
        Restrict access to staff members only.
        """
        return self.request.user.is_staff

    def form_valid(self, form):
        """
        Save changes to the recipe.

        Updates the status based on user input (draft or published).
        """
        form.instance.status = 0 if self.request.POST.get('action') == 'draft' else 1
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the appropriate page after saving changes to a recipe.

        Draft recipes redirect to the home page, and published recipes redirect
        to their detail page.
        """
        return reverse(
            'recipe_detail', kwargs={'slug': self.object.slug}
        ) if self.object.status == 1 else reverse('home')

    def get_context_data(self, **kwargs):
        """
        Add additional context to the recipe editing view.

        Includes a page title for better user experience.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Edit Recipe'
        return context


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for staff members to delete a recipe.
    """
    model = Recipe
    template_name = "blog/recipe_confirm_delete.html"
    success_url = '/'

    def test_func(self):
        """
        Restrict access to staff members only.
        """
        recipe = self.get_object()
        return self.request.user.is_staff

    def get_context_data(self, **kwargs):
        """
        Add additional context to the recipe deletion confirmation view.

        Includes a page title for better user experience.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Recipe?'
        return context


@login_required
def comment_edit(request, slug, comment_id):
    """
    View to allow users to edit their own comments.

    Args:
        request: The HTTP request object.
        slug: The slug of the recipe associated with the comment.
        comment_id: The ID of the comment to edit.

    Returns:
        Redirects the user to the recipe detail page after editing.
    """
    if request.method == "POST":
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            # Save the updated comment but set it to unapproved
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment Updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


@login_required
def comment_delete(request, slug, comment_id):
    """
    View to allow users to delete their own comments.

    Args:
        request: The HTTP request object.
        slug: The slug of the recipe associated with the comment.
        comment_id: The ID of the comment to delete.

    Returns:
        Redirects the user to the recipe detail page after deletion.
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user or request.user.is_staff:
        # Delete the comment if the user is the author or a staff member
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class MyCookbookLoginView(LoginView):
    """
    Login view with a custom page title for better user experience.
    """
    def get_context_data(self, **kwargs):
        """
        Add the page title to the login view context.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Login"
        return context


class MyCookbookLogoutView(LogoutView):
    """
    Logout view with a custom page title for better user experience.
    """
    def get_context_data(self, **kwargs):
        """
        Add the page title to the logout view context.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Logout"
        return context


class MyCookbookSignupView(SignupView):
    """
    Signup view with a custom page title for better user experience.
    """
    def get_context_data(self, **kwargs):
        """
        Add the page title to the signup view context.
        """
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Register"
        return context
