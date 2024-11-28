# Testing

This is the TESTING file for the [My Cookbook](https://pp4-my-cookbook-blog-1667a6d7fc25.herokuapp.com/) website.

Return back to the [README.md](README.md) file.

---

## Table of Contents  

- [Validation](#validation)
  - [HTML Validation](#html-validation)
  - [JavaScript Validation](#javascript-validation)
  - [Python Validation](#python-validation)
  - [CSS Validation](#css-validation)
- [Lighthouse Scores](#lighthouse-scores)
- [Wave Accessibility Evaluation](#wave-accessibility-evaluation)
- [Functionality Testing](#functionality-testing)
  - [Navigation](#navigation)
  - [Authentication](#authentication)
  - [User Authentication Errors](#user-authentication-errors)
  - [Recipe Management](#recipe-management)
  - [Comments](#comments)
  - [Admin Panel](#admin-panel)
    - [Recipe Management](#recipe-management-in-admin-panel)
    - [Comment Management](#comment-management-in-admin-panel)
  - [Social Media Links](#social-media-links)
- [Dev Tools/Real World Device Testing](#dev-toolsreal-world-device-testing)
  - [Dev Tools Device Testing](#dev-tools-device-testing)
  - [Real World Device Testing](#real-world-device-testing)
  - [Browser Compatibility](#browser-compatibility)
- [Bug Fixes](#bug-fixes)

---
<br>

## Validation
---

### HTML Validation

For my HTML files, I have used [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

Due to the usage of Jinja syntax (e.g., `{% extends "base.html" %}` and `{{ form|crispy }}`) and authentication requirements, the following approach was used for validation:

1. Navigate to each individual page via the deployed Heroku app link.
2. Right-click the screen or use `CTRL+U` (`⌘+U` on Mac) to "View page source."
3. Copy the complete HTML code and paste it into the [validate by input](https://validator.w3.org/#validate_by_input) option.
4. Fix any errors or warnings, revalidate, and record results.

<details>

<summary> View HTML Validation </summary>

![HTML Validation](/docs/testing/testing-images/html-css-js/html-all-clear.png)

</details>

<br>

All pages passed validation except:
- **Add/Edit Recipe pages:** Errors due to SummerNote and Django Forms code.
- **Sign-Up page:** Errors related to Django Forms.

| **HTML Source Code/Page**         | **Errors**      | **Warnings** |
|------------------------------------|-----------------|--------------|
| Home                               | 0               | 0            |
| Sign In                            | 0               | 0            |
| Sign Up                            | [4](/docs/testing/testing-images/html-css-js/html-sign-up-errors.png) | 0 |
| Recipe Detail                      | 0               | 0            |
| Add/Edit Recipe | 18 - [1](/docs/testing/testing-images/html-css-js/html-add-edit-recipe-errors-1.png), [2](/docs/testing/testing-images/html-css-js/html-add-edit-recipe-errors-2.png), [3](/docs/testing/testing-images/html-css-js/html-add-edit-recipe-errors-3.png) | 0 |
| Delete Recipe                      | 0               | 0            |
| Edit Comment                       | 0               | 0            |
| Delete Comment                     | 0               | 0            |
| Team Page                          | 0               | 0            |
| Search Results                     | 0               | 0            |
| Search Results (if empty)          | 0               | 0            |
| Error 403                          | 0               | 0            |
| Error 404                          | 0               | 0            |
| Error 405                          | 0               | 0            |
| Error 500                          | 0               | 0            |

---

### JavaScript Validation

I used [JSHint](https://jshint.com/) to validate JavaScript code for the comment section buttons.

<details>

<summary> View JS validation results </summary>

| **Page**              | **Screenshot**                                                     | **Errors** | **Warnings** |
|-----------------------|--------------------------------------------------------------------|------------|--------------|
| `recipe_detail.html`  | ![JavaScript Validation](/docs/testing/testing-images/html-css-js/jshint-comments-js.png) | None       | None         |

</details>

---

### Python Validation

The following Python files were validated and found to be error-free.

| **Feature**            | **admin.py**                     | **forms.py**                     | **models.py**                   | **urls.py**                     | **views.py**                     | **settings.py**                  |
|------------------------|-----------------------------------|-----------------------------------|----------------------------------|----------------------------------|-----------------------------------|----------------------------------|
| My Cookbook Main App   | N/A                              | N/A                              | N/A                             | [No errors](/docs/testing/testing-images/my-cookbook/python-my-cookbook-urls.png) | [No errors](/docs/testing/testing-images/my-cookbook/python-my-cookbook-views.png) | [No errors](/docs/testing/testing-images/my-cookbook/python-mycookbook-settings.png) |
| Blog (Recipes)         | [No errors](/docs/testing/testing-images/blog/python-blog-admin.png) | [No errors](/docs/testing/testing-images/blog/python-blog-forms.png) | [No errors](/docs/testing/testing-images/blog/python-blog-models.png) | [No errors](/docs/testing/testing-images/blog/python-blog-urls.png) | [No errors](/docs/testing/testing-images/blog/python-blog-views.png) | N/A |
| Team (Team Members)    | [No errors](/docs/testing/testing-images/team/python-team-admin.png) | N/A                              | [No errors](/docs/testing/testing-images/team/python-team-models.png) | [No errors](/docs/testing/testing-images/team/python-team-urls.png) | [No errors](/docs/testing/testing-images/team/python-team-views.png) | N/A |

---

### CSS Validation

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used for validation. External CSS from the Bootstrap CDN was excluded. Minor warnings were related to the use of CSS variables for colors and fonts.

<details>

<summary> View CSS Validation</summary>

![CSS Validation](/docs/testing/testing-images/html-css-js/css-validation.png)

</details>

---
<br>

## Lighthouse Scores
---

Lighthouse testing was conducted in Incognito mode for accurate results.


### Desktop

<details>

<summary> Home Page (Recipe List) </summary>

![Lighthouse Desktop](/docs/testing/testing-images/lighthouse/lighthouse-index-desktop.png)

</details>
<details>

<summary> Recipe Detail  </summary>

![Lighthouse Desktop](/docs/testing/testing-images/lighthouse/lighthouse-recipe-detail-desktop.png)

</details>
<details>

<summary> Team Page </summary>

![Lighthouse Desktop](/docs/testing/testing-images/lighthouse/lighthouse-team-desktop.png)

</details>


### Mobile

<details>

<summary> Home Page (Recipe List) </summary>

![Lighthouse Mobile](/docs/testing/testing-images/lighthouse/lighthouse-index-mobile.png)

</details>
<details>

<summary> Recipe Detail Page </summary>

![Lighthouse Mobile](/docs/testing/testing-images/lighthouse/lighthouse-recipe-detail-mobile.png)

</details>
<details>

<summary> Team Page </summary>

![Lighthouse Mobile](/docs/testing/testing-images/lighthouse/lighthouse-team-mobile.png)

</details>
  
---
<br>

## Wave Accessibility Evaluation
---

Using the WAVE Accessibility Tool, I identified minor issues related to color contrast and made changes accordingly.  All pages have no errors with the following exceptions:
- There are 4 consistent errors across the site due to the logos in the footer - the WAVE Tool registers them as being empty `<a>` tags. 
- The faded appearance of a pre-approved comment causes contrast issues.  I will explore other ways around this in future development. 


<details>
<summary> Home Page (Recipe List) </summary>

![Home page](/docs/testing/testing-images/wave/wave-recipe-list-1.png)
![Home page](/docs/testing/testing-images/wave/wave-recipe-list-2.png)

</details>
<details>

<summary> Recipe Detail </summary>

![Recipe Detail](/docs/testing/testing-images/wave/wave-recipe-detail-contrast-errors-1.png)
![Recipe Detail](/docs/testing/testing-images/wave/wave-recipe-detail-contrast-errors-2.png)
![Recipe Detail](/docs/testing/testing-images/wave/wave-recipe-detail-contrast-errors-3.png)

</details>
<details>

<summary> Team Page </summary>

![Team page](/docs/testing/testing-images/wave/wave-team.png)

</details>
<details>

<summary> Add Recipe form </summary>

![Add recipe form](/docs/testing/testing-images/wave/wave-add-recipe.png)

</details>

---
<br>

## Functionality Testing
---

Details of manual testing of the functions of each feature of the website. Chrome DevTools was used to test the website on different screen sizes.

---

### Navigation

| Test Label            | Test Action                                             | Expected Outcome                                                                 | Test Outcome |
|-----------------------|--------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Navigation links      | Click all links in navigation menu on each page.       | Each link leads to expected page from any page.                                 |              PASS|
| Navigation menu responsiveness | Resize the screen below and above 768px wide. | Navigation menu collapses into a toggler on screens lower than 768px wide and expands above 768px. |      PASS        |

---

### Authentication

| Test Label     | Test Action                              | Expected Outcome                                         | Test Outcome |
|----------------|------------------------------------------|---------------------------------------------------------|--------------|
| User login     | Log in as registered user.              | User is logged in.                                      |    PASS          |
| User sign up   | Submit sign-up form with required input. | User object created in database.                       |      PASS        |
| User log out   | Log out authenticated user.             | User is logged out.                                     |      PASS        |
| Admin login    | Log in to admin panel with superuser details. | Login successful, user panel accessed.             |     PASS         |

---

### User Authentication Errors

| Test Label      | Test Action                    | Expected Outcome                                               | Test Outcome |
|-----------------|--------------------------------|----------------------------------------------------------------|--------------|
| Wrong Password on Sign In  | Enter an existing username with an incorrect password in the login form and submit. | The form displays an error message. User remains on the login page.  |        PASS          |
| Nonexistent Username on Sign In  | Enter an non-existent username in the login form and submit. | The form displays an error message. User remains on the login page.  |      PASS            |
| Non-original Username on Sign Up | Attempt to sign up with a username that already exists in the database.                                  | The form displays an error message. User is not signed up. |      PASS            |
| Unmatching Passwords on Sign Up | Enter mismatched passwords in the password and confirm password fields of the sign-up form and submit.      | The form displays an error message. User is not signed up.                 |       PASS           |
| Too Short Password on Sign Up    | Enter a password that is shorter than the minimum required length in the sign-up form and submit.           | The form displays an error message. User is not signed up.                  |        PASS          |
| Invalid Email Address on Sign Up | Enter an invalid email address (e.g., missing '@') in the email field of the sign-up form and submit.        | The form displays an error message. User is not signed up.            |        PASS          |

---

### Recipe Management

| Test Label                         | Test Action                                                                                 | Expected Outcome                                                                 | Test Outcome |
|------------------------------------|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Pagination                         | View list view with more than 8 recipes displayed.                                          | 8 recipes are displayed per page with page links below.                         |     PASS         |
| Recipe cards as links              | Click recipe cards.                                                                        | Directed to full recipe details.                                               |    PASS          |
| Recipe form required fields        | Click submit button on create recipe form before entering a value for each field.          | Empty fields for title, cooking time, serves, ingredients, and method raise validation error, and form cannot be submitted. |      PASS        |
| Submit recipe for publication      | Submit a recipe with all required inputs and click 'Publish'.                              | Successful form submission, recipe published, recipe object added to database. User redirected to recipe_detail page for new recipe. |     PASS         |
| Submit recipe for draft            | Submit a recipe with all required inputs and click 'Save as Draft'.                        | Successful form submission, recipe object added to database. User redirected to recipe list view. |      PASS        |
| Edit recipe form field population  | Click 'edit' button in recipe when staff member is logged in.                              | Recipe form loads with the fields populated with the data from the recipe being edited. |      PASS        |
| Edit recipes and submit for publication | Click 'edit' button in recipe when staff member is logged in, change data in the fields, and submit form by clicking 'publish' or 'save as draft'. | Successful form submission, recipe object edited in database. User redirected to appropriate page. |      PASS        |
| Delete recipe button               | Click 'delete' button in recipe when staff member is logged in.                            | User is directed to confirm delete page.                                       |     PASS         |
| Confirm delete                     | Click 'delete' button in recipe when staff member is logged in, click 'confirm' button on confirm delete page. | Recipe object is successfully removed from database, the user is redirected to the recipe list view, and a message in displayed confirming successful deletion. |     PASS         |
| Cancel delete                      | Click 'delete' button in recipe when staff member is logged in, click 'cancel' button on deletion confirmation page. | User is returned to full recipe details page and recipe object is not deleted from database. |     PASS         |

---

### Comments

| Test Label               | Test Action                                                                    | Expected Outcome                                                                 | Test Outcome |
|--------------------------|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Comment form logged in   | View full recipe details as authenticated user.                               | Comment form is displayed under the recipe.                                     |   PASS           |
| Comment form not logged in| View full recipe details as anonymous user.                                   | Comment form is not displayed.                                                 |     PASS         |
| Submit comment           | View full recipe details as authenticated user and submit a comment.          | Comment form successfully submitted and message informing user comment is awaiting approval is displayed. Comment object created in database. |      PASS        |
| View comments            | View full recipe details of recipe with comments.                            | Comments are displayed in the order they were created.                         |     PASS         |

---

### Admin Panel

#### Recipe Management

| Test Label              | Test Action                                            | Expected Outcome                                                                 | Test Outcome |
|-------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Recipe management list  | View recipe management page in admin panel.           | Recipe model fields displayed in list include title, slug, author, description, status, servings, ingredients, method, and image field. |    PASS          |
| Recipe management filter| Click options in filter menu on recipe management page in admin panel. | Recipe can be filtered by status choices.                                       |      PASS        |
| Recipe management search| Enter search terms in search bar and click search.    | Recipes can be searched by keywords in title and description.                   |      PASS        |

#### Comment Management

| Test Label                | Test Action                                                            | Expected Outcome                                                                 | Test Outcome |
|---------------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|--------------|
| Comment management list   | View comment management page in admin panel.                         | Comment model fields displayed in list include recipe, body, author, created_on.|       PASS       |
| Comment management filter | Click options in filter menu on comment management page in admin panel. | Comments can be filtered by recipe and created_on.                              |      PASS        |
| Comment management approve action | Click checkbox for multiple comments pending approval, select 'approve comments' from action dropdown and click go. | All checked comments approved.                                                  |     PASS         |
| Comment management search | Enter search terms in search bar and click search.                   | Comments can be searched by keywords in body, recipe title, and user name.      |    PASS          |

---

### Social Media Links

| Test Label         | Test Action                           | Expected Outcome                                                    | Test Outcome |
|--------------------|---------------------------------------|----------------------------------------------------------------------|--------------|
| Social media links | Click all social media links in the footer. | Appropriate social media platform websites will open in a new tab.   |      PASS        |

---
<br>

## Dev Tools/Real World Device Testing
---

Responsiveness testing was carried out using Google Dev Tools on the devices detailed within the below table. Responsiveness was evident on all features throughout all tested devices. 
  
<br>

### Dev Tools Device Testing - all features tested, issues noted below

| Device  | Feature    | Issue  | Fix  |
| ------- | ---------- | ------ |------|
| iPhone SE | Sign Up and Sign in pages | Pages looked cramped | Added margins to Sign Up heading and to sign-up/in button |
| Nest Hub Max | All features | No issues | None needed |
| iPad Mini | All features | No issues | None needed |
| Asus Zenbook Fold | Scroll down | Can't see footer | This is a browser issue and not a responsivity issue |
   
<br>

### Real World Device Testing

| Device      | Feature    | Issue  | Fix  | 
| ------------| ---------- | ------ |------|
| Samsung S9 | Team Page | Scroll bar on team member bio | Separate media queries created for screens max-width: 400px and 300px to cope with smaller screens (bio font size reduced) |
| iPad Pro (2020) | All features |  No issues  | None needed |
| HP 15S laptop  | All features | No issues | None needed |
| iPad Pro 2021 |    All features      |    No issues    |  None needed |
| Google Pixel 6 | All features | No issues | None needed |
| Samsung S22 | All features | No issues | None needed |


### Browser Compatibility

My Cookbook was tested on the following browsers - new users were created, recipes/comments added and updated/deleted and all features were tested.  No issues were found.

- Chrome v 131.0.6778.86 
- Firefox v 133.0
- Edge v 129.0.2792.89
- Safari v17.6 

---
<br>

## Bug Fixes
---

|Bug|Solution|Fixed?|
|-----|-----|-----|
|Placeholder images not showing in recipe list | Updated featured_image field in model to have a cloudinary url rather than using a static file. Used python shell to update recipes that were already in database. | Yes | 
|Second page of recipes not showing - I had managed to save a recipe without automatically creating a slug - I navigated off the page before saving it properly but it still saved as a draft. | Use the shell to identify and fix recipes missing slugs. Add safeguard in AddRecipe view to make sure slugs are always created. Add a check for a slug in the index.html template to prevent the page breaking if there is no slug| Yes |
|Recipe Detail not showing for draft recipes|Update recipe_detail view to include draft recipes if the logged-in user is the author|Yes|
|Current image file not displaying in edit_recipe.html|Render each form field separately rather than as one crispy form|Yes|
|Team page not showing - KeyError at /team/|Return default queryset for all Team Members and then split the queryset in get_context_data|Yes|
|Blank spaces in index.html (draft recipes)|Filter recipes in the backend rather than using css to hide them|Yes|
|Admin panel not displaying - slug:slug/ pattern was catching the /admin/ route when it was included at the project-level via path(' ',include('blog.urls'))|Updated app-level urls.py to make the patterns more specific, so they don’t unintentionally catch /admin/ or other URLs - changed to /recipe/slug:slug/ which avoids clashing with /admin/|Yes|


**There were no other known bugs at the time of submitting the project.**