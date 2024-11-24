# Functionality Testing

Details of manual testing of the functions of each feature of the website. Chrome DevTools was used to test the website on different screen sizes.

---

## Navigation

| Test Label            | Test Action                                             | Expected Outcome                                                                 | Test Outcome |
|-----------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Navigation links      | Click all links in navigation menu on each page.       | Each link leads to expected page from any page.                                 |              |
| Navigation menu responsiveness | Resize the screen below and above 768px wide. | Navigation menu collapses into a toggler on screens lower than 768px wide and expands above 768px. |              |

---

## Authentication

| Test Label     | Test Action                              | Expected Outcome                                         | Test Outcome |
|----------------|------------------------------------------|---------------------------------------------------------|--------------|
| User login     | Log in as registered user.              | User is logged in.                                      |              |
| User sign up   | Submit sign-up form with required input. | User object created in database.                       |              |
| User log out   | Log out authenticated user.             | User is logged out.                                     |              |
| Admin login    | Log in to admin panel with superuser details. | Login successful, user panel accessed.             |              |

---

## Recipe Management

| Test Label                         | Test Action                                                                                 | Expected Outcome                                                                 | Test Outcome |
|------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Pagination                         | View list view with more than 8 recipes displayed.                                          | 8 recipes are displayed per page with page links below.                         |              |
| Recipe cards as links              | Click recipe cards.                                                                        | Directed to full recipe details.                                               |              |
| Recipe form required fields        | Click submit button on create recipe form before entering a value for each field.          | Empty fields for title, cooking time, serves, ingredients, and method raise validation error, and form cannot be submitted. |              |
| Submit recipe for publication      | Submit a recipe with all required inputs and click 'Publish'.                              | Successful form submission, recipe published, recipe object added to database. User redirected to recipe_detail page for new recipe. |              |
| Submit recipe for draft            | Submit a recipe with all required inputs and click 'Save as Draft'.                        | Successful form submission, recipe object added to database. User redirected to recipe list view. |              |
| Edit recipe form field population  | Click 'edit' button in recipe when staff member is logged in.                              | Recipe form loads with the fields populated with the data from the recipe being edited. |              |
| Edit recipes and submit for publication | Click 'edit' button in recipe when staff member is logged in, change data in the fields, and submit form by clicking 'publish' or 'save as draft'. | Successful form submission, recipe object edited in database. User redirected to appropriate page. |              |
| Delete recipe button               | Click 'delete' button in recipe when staff member is logged in.                            | User is directed to confirm delete page.                                       |              |
| Confirm delete                     | Click 'delete' button in recipe when staff member is logged in, click 'confirm' button on confirm delete page. | Recipe object is successfully removed from database, the user is redirected to the recipe list view, and a message in displayed confirming successful deletion. |              |
| Cancel delete                      | Click 'delete' button in recipe when staff member is logged in, click 'cancel' button on deletion confirmation page. | User is returned to full recipe details page and recipe object is not deleted from database. |              |

---

## Comments

| Test Label               | Test Action                                                                    | Expected Outcome                                                                 | Test Outcome |
|--------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Comment form logged in   | View full recipe details as authenticated user.                               | Comment form is displayed under the recipe.                                     |              |
| Comment form not logged in| View full recipe details as anonymous user.                                   | Comment form is not displayed.                                                 |              |
| Submit comment           | View full recipe details as authenticated user and submit a comment.          | Comment form successfully submitted and message informing user comment is awaiting approval is displayed. Comment object created in database. |              |
| View comments            | View full recipe details of recipe with comments.                            | Comments are displayed in the order they were created.                         |              |

---

## Admin Panel

### Recipe Management

| Test Label              | Test Action                                            | Expected Outcome                                                                 | Test Outcome |
|-------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Recipe management list  | View recipe management page in admin panel.           | Recipe model fields displayed in list include title, slug, author, description, status, servings, ingredients, method, and image field. |              |
| Recipe management filter| Click options in filter menu on recipe management page in admin panel. | Recipe can be filtered by status choices.                                       |              |
| Recipe management search| Enter search terms in search bar and click search.    | Recipes can be searched by keywords in title and description.                   |              |

### Comment Management

| Test Label                | Test Action                                                            | Expected Outcome                                                                 | Test Outcome |
|---------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Comment management list   | View comment management page in admin panel.                         | Comment model fields displayed in list include recipe, body, author, created_on.|              |
| Comment management filter | Click options in filter menu on comment management page in admin panel. | Comments can be filtered by recipe and created_on.                              |              |
| Comment management approve action | Click checkbox for multiple comments pending approval, select 'approve comments' from action dropdown and click go. | All checked comments approved.                                                  |              |
| Comment management search | Enter search terms in search bar and click search.                   | Comments can be searched by keywords in body, recipe title, and user name.      |              |

---

## Social Media Links

| Test Label         | Test Action                           | Expected Outcome                                                    | Test Outcome |
|--------------------|---------------------------------------|----------------------------------------------------------------------|--------------|
| Social media links | Click all social media links in the footer. | Appropriate social media platform websites will open in a new tab.   |              |
