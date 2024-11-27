# My Cookbook - Recipe Blog

## Intro

For my fourth portfolio project, I created a blog app to display recipes to a user.  As a private chef, I often get asked by clients to share my recipes with them.  My Cookbook facilitates this as a recipe-sharing app that allows users to browse, search, and interact with recipes - without having to scroll through a lot of text first.

![My Cookbook responsive screenshot](docs/images/am-i-responsive.png)

Visit the deployed site here: [My Cookbook](https://pp4-my-cookbook-blog-1667a6d7fc25.herokuapp.com/)

View My Cookbook on [Github](https://github.com/EJFleet/pp4-my-cookbook-blog)

For Admin access with relevant sign-in information: [My Cookbook Admin](https://pp4-my-cookbook-blog-1667a6d7fc25.herokuapp.com/admin/)

![GitHub last commit](https://img.shields.io/github/last-commit/EJFleet/pp4-my-cookbook-blog)
![GitHub language count](https://img.shields.io/github/languages/count/EJFleet/pp4-my-cookbook-blog)
![GitHub top language](https://img.shields.io/github/languages/top/EJFleet/pp4-my-cookbook-blog)


---

* [User Experience (UX)](#user-experience-ux)
  * [User Stories](#user-stories)
  * [Design](#design)
    * [Planning](#planning)
    * [Imagery](#imagery)

* [Features](#features)
  * [Future Implementations](#future-implementations)

* [Project Management & Agile Methodologies](#project-management--agile-methodologies)
  * [Kanban Board](#kanban-board)
  * [MoSCoW Prioritisation](#moscow-prioritisation)

* [Technologies Used](#technologies-used)
  * [Languages](#languages)
  * [Frameworks, Libraries & Packages](#frameworks-libraries--packages)
  * [Tools](#tools)

* [Deployment & Local Development](#deployment--local-development)
  * [Forking the GitHub Repository](#forking-the-github-repository)
  * [Cloning the GitHub Repository](#cloning-the-github-repository)
  * [Deploying to Heroku](#deploying-to-heroku)

* [Testing](#testing)
  * [Functionality](#functionality)
  * [Code Validation](#code-validation)
  * [Bug Fixes](#bug-fixes)

* [Credits](#credits)
  * [Code Inspiration](#code-inspiration)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

The user experience (UX) for this project was designed with careful consideration of user needs and project goals, ensuring a seamless, intuitive, and engaging experience for all users. The planning process was informed by Agile methodologies and centered around user stories, categorized into epics to structure development priorities effectively.

<details>

<summary> Epics and User Stories screenshot </summary>

![Epics and User Stories screenshot](docs/images/epics-and-user-stories.png)

</details>

[Link to original document](https://docs.google.com/spreadsheets/d/1zJu0cbOBp-2E82P60fr14d2KqF_FlaW7Y0sWi2PrPls/edit?usp=sharing)

  ### User Stories

  #### Navigation

  As a user I can:
  - use a simple navigation menu so that easily find content.
  - view the navigation menu on any screen sizes so that navigating the site remains easy on all my devices.
  - easily find social media links so that I can find and interact with a community of app users.


  #### User Account

  As a Site User I can:
  - sign up for an account so that I can interact with site content by leaving comments.
  - easily sign in to my account so that I can easily use the site features on return visits.
  - easily log out of my account so that I can keep my account secure.

  As a Site Admin I can:
  - delete a User's account so that I can remove any inappropriate accounts.


  #### Recipe CRUD

    
  As a Staff Member I can:
  - create recipes so that I can share them on the site.
  - save a recipe as a draft so that I can make changes later.
  - publish and unpublish recipes so that I can choose whether to share the recipe or not.
  - update/edit recipes so that I can revise the recipe.
  - delete recipes so that I can remove the recipe from the site.


  #### Site Features

  As a Site User I can:
  - view a paginated list of recipes so that I can select one to read.
  - click on a recipe so that I can read the full recipe.
  - view a list of team members so that I can see who is behind the blog.
  - search for recipe so that I can find the relevant recipe for my needs.


  #### Comment CRUD

  As a Site User I can:
  - view a list of approved comments by registered users so that I can see tips and opinions on each recipe.
  
  As a logged-in Site User I can:
  - leave comments on a recipe so that I can be involved in the conversation.
  - see a notification that my comment is waiting for approval so that I know it has been sent.
  - see my comment displayed just in my view before it has been approved so that I can make any necessary changes.
  - edit my own comments so that I can correct any mistakes.
  - delete my own comments so that I can decide whether I want them to be public any more or not.

  As a Site Admin I can:
  - decide whether to approve or delete a User's comment so that no inappropriate content is displayed on my website.


  #### Team Members

  As a Site Admin I can:
  - create a new Team Member so that I can add a new member of staff as the team grows.
  - edit a Team Member so that I can keep content relevant if someone's details change.
  - delete a Team Member so that I can keep content relevant if somebody leaves. 


### Design

#### Planning

##### Structure

The Recipe Book app is designed with a simple structure to ensure the app is easy to use and navigate. Each page has a consistent layout to allow users to easily find the information they need. The app has a responsive design to ensure it can be clearly viewed on a wide range of devices. The navigation menu is available on all pages of the app to provide users with a consistent method to navigate the site. Bootstrap rows and columns have been used to provide a clean and uniform structure to the content of each page.

##### Wireframes

The wireframes that I originally designed have slightly different aesthetic differences to the finished product. During the construction process, I decided to change the format and layout of some of the features. The original wireframes are below - though the concept evolved, the original layout is still relevant and can be recognised in the finished site.

<details>

<summary> base.html - desktop and mobile </summary>

![base.html - desktop and mobile](docs/wireframes/mycookbook-base-pc-and-smartphone.png)

</details>

<details>

<summary> index.html - desktop and mobile -relevant for both the recipe list and the team page </summary>

![index.html - PC and mobile](docs/wireframes/mycookbook-index-pc-and-smartphone.png)

</details>

<details>

<summary>recipe_detail.html - desktop</summary>

![recipe_detail.html - desktop](docs/wireframes/mycookbook-recipe-detail-pc.png)

</details>

<details>

<summary>recipe_detail.html - mobile</summary>

![recipe_detail.html - mobile](docs/wireframes/mycookbook-recipe-detail-smartphone.png)

</details>


#### Database Design

The database design for this project consists of the following models:
- **Recipe**: Represents individual recipes.
- **Comment**: Represents comments on recipes.
- **TeamMember**: Represents staff members contributing to the site.


### Database Evolution

The initial Entity Relationship Diagram (ERD) was created during the planning phase to represent the anticipated relationships between the models. However, as development progressed, certain requirements and challenges emerged that led to changes in the database structure. This is a common aspect of Agile development, allowing flexibility to adapt to new insights.

<details>

<summary> Current ERD  </summary>
  
![Current ERD](docs/images/current-erd.png)

</details>

<details>

<summary> Original ERD </summary>

![Original ERD](docs/images/first-edition-erd.png)

</details>


#### Colour Scheme

The colour scheme was chosen to give a fresh, clean look to the app that does not distract from the text and images of the recipes and to provide contrast for good readability of the information. The colour palette was created using [Coolors](https://coolors.co/).

<details>

<summary> Colour Palette  </summary>

  
![Colour Palette](docs/images/coolors-colour-palette-s.png)

</details>


#### Fonts
  
[Google Fonts](https://fonts.google.com/) was used to add the following fonts:

- 'Roboto' was used to provide a simple, clean and easy to read appearance.
- 'Nixie One' was used to give character to the logo. 


#### Imagery

- All images used for the recipes were taken from [BBC Good Food](https://bbcgoodfood.com) and [Recipe Tin Eats](https://recipetineats.com).
- All images used for the team members were downloaded for free from [Pexels](https://pexels.com)

  <details>

  <summary>Favicon was created using <a href="https://favicon.io">favicon.io</a></summary>
    
  ![Favicon](static/favicons/favicon-32x32.png)

  </details>


---

## Features

### General Features

#### Navigation Bar

The site features a responsive navigation bar that is consistent across all pages.
<details>

<summary> Details </summary>
It includes links to the following pages:
- Home
- Register, Login/Logout (based on user authentication status)
- Meet the Team
- Add Recipe

It also includes:
- the app logo
- the app slogan of 'Recipes for Everyday Living'
- a search bar 

**Key Features**:
- Fixed to the top of the screen in all views to allow for easy navigation.
- Adjusts automatically for different screen sizes.
- On smaller screens, it collapses into a dropdown toggler for a cleaner and more user-friendly interface.

**Screenshots**:
![Navigation Bar Desktop View - logged in](docs/images/features/navbar/navbar-desktop-logged-in.png)
![Navigation Bar Mobile View - logged in](docs/images/features/navbar/navmenu-mobile-logged-in.png)
![Navigation Bar Desktop View - logged out](docs/images/features/navbar/navbar-desktop-logged-out.png)
![Navigation Bar Mobile View - logged out](docs/images/features/navbar/navbar-mobile-logged-out.png)

</details>


---

#### Footer
The site displays a footer on all pages which is fully responsive at all screen sizes.

<details>

<summary> Details </summary>

It provides quick access to:
- Copyright information for the site.
- Social media links (Facebook, X, Instagram, YouTube).

**Key Features**:
- Social media icons open in a new tab when clicked.
- The footer is fully responsive and adjusts to fit any screen size.

**Screenshots**:
![Footer Desktop View](docs/images/features/footer/footer-desktop.png)
![Footer Mobile View](docs/images/features/footer/footer-mobile.png)

</details>

---
### Recipe Features

#### Recipe List View
The recipe list view displays all available recipes in a paginated format. Users can browse through the recipes to find one they are interested in.

<details>

<summary> Details </summary>

**Key Features**:
- Pagination: Limits the number of recipes displayed per page for better user experience.
- Each recipe card displays:
  - Recipe title
  - Thumbnail image
  - Short description
  - Date on which the recipe was posted
- Clicking on a recipe card redirects the user to the full recipe details page.
- If a user is not a logged-in Staff user, draft recipes are hidden from display.  Otherwise, drafts are shown with a faded effect.

**Screenshots**:

Desktop:
![Recipe List Desktop View - top ](docs/images/features/recipe-list/recipe-list-top-desktop.png)
![Recipe List Desktop View - bottom](docs/images/features/recipe-list/recipe-list-bottom-desktop.png)

Mobile:
![Recipe List Mobile View - top](docs/images/features/recipe-list/recipe-list-mobile.png)
![Recipe List Mobile View - bottom](docs/images/features/recipe-list/recipe-list-bottom-mobile.png)

Example of draft recipe display (2nd from left):
![Draft recipe](docs/images/features/recipe-list/recipe-list-top-desktop-drafts.png)

</details>

---

#### Recipe Details
The recipe details page provides complete information about a selected recipe.

<details>

<summary> Details </summary>

**Key Features**:
- Displays:
  - Recipe title, description, servings, ingredients, and method.
  - Featured image (or placeholder if no image is provided).
  - Author and date of creation.
- Comment section below the recipe.
- Icon showing the comment count on the recipe.
- Comment form or a link to log in, depending on user status.

**Screenshots**:

Anonymous User (Desktop):

![Recipe Detail Desktop View - Anonymous User](docs/images/features/recipe-detail/recipe-detail-desktop-top-not-logged-in.png)
![Recipe Detail Desktop View - Anonymous User](docs/images/features/recipe-detail/recipe-detail-desktop-middle-not-logged-in.png)
![Recipe Detail Desktop View - Anonymous User](docs/images/features/recipe-detail/recipe-detail-desktop-bottom-not-logged-in.png)

Logged-in Non-Staff User (Desktop):

![Recipe Detail Desktop View - Non-Staff User](docs/images/features/recipe-detail/recipe-detail-desktop-top-logged-in-non-staff.png)
![Recipe Detail Desktop View - Non-Staff User](docs/images/features/recipe-detail/recipe-detail-desktop-middle-logged-in-non-staff.png)
![Recipe Detail Desktop View - Non-Staff User](docs/images/features/recipe-detail/recipe-detail-desktop-bottom-logged-in-non-staff.png)

Logged-in Staff User (Desktop):

![Recipe Detail Desktop View - Staff User](docs/images/features/recipe-detail/recipe-detail-desktop-top.png)
![Recipe Detail Desktop View - Staff User](docs/images/features/recipe-detail/recipe-detail-desktop-middle.png)
![Recipe Detail Desktop View - Staff User](docs/images/features/recipe-detail/recipe-detail-desktop-bottom-no-comments-logged-in.png)

Anonymous User (Mobile):

![Recipe Detail Mobile View - Anonymous User](docs/images/features/recipe-detail/recipe-detail-mobile-top-not-logged-in.png)
![Recipe Detail Mobile View - Anonymous User](docs/images/features/recipe-detail/recipe-detail-mobile-bottom-not-logged-in.png)

Logged-in Non-Staff User (Mobile):

![Recipe Detail Mobile View - Non-Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-top-non-staff.png)
![Recipe Detail Mobile View - Non-Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-middle-non-staff.png)
![Recipe Detail Mobile View - Non-Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-bottom-non-staff.png)

Logged-in Staff User (Mobile):

![Recipe Detail Mobile View - Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-top.png)
![Recipe Detail Mobile View - Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-middle-logged-in.png)
![Recipe Detail Mobile View - Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-middle-2-logged-in.png)
![Recipe Detail Mobile View - Staff User](docs/images/features/recipe-detail/recipe-detail-mobile-bottome-logged-in.png)

</details>

---

#### Recipe Management (Admin/Staff Only)
Staff and admin users can manage recipes directly from the site or the admin panel.

<details>

<summary> Details </summary>

**Key Features**:
- **Create Recipe**: Staff can create a new recipe with fields for title, description, ingredients, method, servings and image.
- **Save as Draft or Publish**: Recipes can be saved as drafts for future editing or published immediately.
- **Edit Recipe**: Staff can update any aspect of the recipe, including changing its status (draft or published).
- **Delete Recipe**: Staff can permanently delete a recipe.

**Screenshots**:

- Create Recipe Form: 

![Create Recipe Form](docs/images/features/recipe-add-edit/form-recipe-add.png)
![Create Recipe Form](docs/images/features/recipe-add-edit/form-recipe-add-2.png)

- Edit Recipe Form: 

This is the same as the form for creating a recipe, except that it is prepopulated with the recipe details.

![Edit Recipe Form](docs/images/features/recipe-add-edit/edit-recipe-1.png)
![Edit Recipe Form](docs/images/features/recipe-add-edit/edit-recipe-2.png)

</details>

---
### Comments Features

#### Comment Section
Users can view comments left by others under each recipe. The comments section provides a way for users to interact and share their thoughts or tips about the recipe.

<details>

<summary> Details </summary>

**Key Features**:

- Comments are displayed in chronological order (newest first).

**Screenshots**:

Staff member:

![Comments Section Desktop View](docs/images/features/comments/comments-desktop-logged-in-staff.png)
![Comments Section Mobile View](docs/images/features/comments/comments-mobile-logged-in-staff.png)

Logged-in User (comment author):

![Comments Section Desktop View](docs/images/features/comments/comments-desktop-logged-in-staff.png)
![Comments Section Mobile View](docs/images/features/comments/comments-mobile-logged-in-user.png)

Logged-in User (not comment author):

![Comments Section Desktop View](docs/images/features/comments/comments-desktop-logged-in-user-not-commenter.png)
![Comments Section Mobile View](docs/images/features/comments/comments-mobile-logged-in-user-not-commenter.png)

Anonymous User:

![Comments Section Desktop View](docs/images/features/comments/comments-desktop-anon-user.png)
![Comments Section Mobile View](docs/images/features/comments/comments-mobile-anon-user.png)


</details>

---

#### Add a Comment
Registered users can leave their own comments on recipes to share their feedback or suggestions.

<details>

<summary> Details </summary>

**Key Features**:

- A form allows users to enter their comments.
- Comments are submitted for admin approval before they become visible to others.
- The user is notified that their comment has been submitted and is waiting for approval.
- Pending comments display a notification to the user below the header that their comment is awaiting approval.

**Desktop**:

![Comment Approval Notication](docs/images/features/comments/comment-desktop-submitted-approval.png)

**Mobile**:

![Comment Approval Notication](docs/images/features/comments/comment-mobile-submitted-approval.png)

</details>

---

#### Edit/Delete Comments
Users have the ability to manage their own comments, while admins have extended privileges to moderate all comments.

<details>

<summary> Details </summary>

**Key Features**:

- **Users**:
  - Edit their own comments to fix errors or make updates.
  - Delete their own comments if they no longer want them displayed.
  - The form for editing comments is the same as the one for adding comments, with the comment populated in the form.

- **Admins**:
  - Delete comments submitted by any user to ensure content adheres to site guidelines.
  - Edit comments (admin only) for minor adjustments if needed.
  - Approve comments (admin only) so that only suitable comments are published.

**Desktop**:

![Edit Comment Form](docs/images/features/comments/comments-desktop-update.png)

**Mobile**:

![Edit Comment Form](docs/images/features/comments/comments-mobile-update.png)

**Admin Comments Panel**:

![Admin Comment Approval](docs/images/features/comments/comments-admin-listview.png)

![Admin Comment Approval](docs/images/features/comments/comments-admin.png)

</details>

### **User Account Features**

#### **Registration**
Users can sign up for an account to access additional features such as leaving comments.

<details>

<summary> Details </summary>

**Key Features**:
- A registration form with fields for username, email, and password.
- Password validation to ensure security.

**Screenshots**:

Desktop:

![Registration Form](docs/images/features/user-accounts/accounts-desktop-registration-form.png)

Mobile:

![Registration Form](docs/images/features/user-accounts/accounts-mobile-registration-form.png)

</details>


---

#### **Login/Logout**

Users can securely log in and out of their accounts to maintain session integrity.

<details>

<summary> Details </summary>

**Key Features**:

- Login form that authenticates users using their credentials.
- A logout option available in the navigation bar when logged in.
- Login status displayed in the top right of the page under the navbar.
- Success messages displayed upon logging in or logging out.


**Screenshots**:

Desktop Login Form:

![Login Form](docs/images/features/user-accounts/accounts-desktop-sign-in-form.png)

Mobile Login Form:

![Login Form](docs/images/features/user-accounts/accounts-mobile-sign-in-form.png)

Desktop Logout Form:

![Logout Form](docs/images/features/user-accounts/accounts-desktop-sign-out.png)

Mobile Logout Form:

![Logout Form](docs/images/features/user-accounts/accounts-mobile-sign-out.png)

Desktop Logged-in Status:

![Login Status](docs/images/features/user-accounts/accounts-desktop-logged-in.png)

Mobile Logged-out Status:

![Logged Out Status](docs/images/features/user-accounts/accounts-mobile-logged-out.png)

Login Confirmation:
![Login Confirmation](docs/images/features/user-accounts/accounts-desktop-sign-in-confirmation.png)

Logout Confirmation:
![Logout Confirmation](docs/images/features/user-accounts/accounts-desktop-sign-out-confirmation.png)


</details>

---


### **Admin/Staff-Specific Features**

#### **Admin Panel**
Admins can manage the site content directly from the Django admin panel.

<details>

<summary> Details </summary>

**Key Features**:
- Manage users, recipes, comments, and team members.
- View and filter data using the admin interface.
- Bulk actions like deleting multiple comments or recipes.

**Screenshots**:
![Admin Panel](docs/images/features/user-accounts/admin-panel.png)

</details>

---

#### **Staff Permissions**
Certain features are restricted to staff or admin users only.

<details>

<summary> Details </summary>

**Key Features**:
- Only staff can create, edit, and delete recipes.
- Only admins can approve or delete comments submitted by users.
- Only admins can add, update or delete a Team Member.


</details>

---

### **Team Member Features**

#### **Team Member Page**
Users can view a dedicated page showcasing the team behind the blog.

<details>

<summary> Details </summary>

**Key Features**:
- Each team member's profile includes their name, job title, bio, location, and image.
- Responsive layout that displays team members attractively on all devices.
- Pagination is applied for easy browsing if there are many team members.

**Screenshots**:

Desktop:

![Team Member Page](docs/images/features/team/team-desktop-top.png)
![Team Member Page](docs/images/features/team/team-desktop-bottom.png)

Mobile:

![Team Member Page](docs/images/features/team/team-mobile-top.png)
![Team Member Page](docs/images/features/team/team-mobile-middle.png)
![Team Member Page](docs/images/features/team/team-mobile-bottom.png)

</details>

---

#### **Manage Team Members**
Admins can manage team member profiles through the admin panel.

<details>

<summary> Details </summary>

**Key Features**:
- Add a new team member with all required details.
- Edit existing team member profiles to keep information up to date.
- Delete team members no longer part of the blog.

**Screenshots**:

![Manage Team Members](docs/images/features/team/team-team-member-admin-list.png)

![Manage Team Members](docs/images/features/team/team-team-member-admin-member.png)

</details>

---

### **Search & Filtering**

#### **Search Recipes**
Users can search for recipes by keywords in their title, description, ingredients or method.

<details>

<summary> Details </summary>

**Key Features**:
- A search box available in the navigation bar on all pages.
- Results dynamically update based on the search query.
- Message displays with search box underneath if no results for search query

**Screenshots**:

Search box Desktop:

![Recipe Search](docs/images/features/search/search-navbar.png)

Search box Mobile:

![Recipe Search](docs/images/features/search/search-navbar-mobile.png)

Search results page for 'cake':

![Recipe Search](docs/images/features/search/search-cake.png)

Zero search results:

![Recipe Search](docs/images/features/search/search-zero.png)



</details>

---
### Error Pages

#### Custom Error Pages

The app provides user-friendly custom error pages for HTTP errors including `403 Forbidden`, `404 Not Found`, `405 Method Not Allowed`, and `500 Internal Server Error`. This ensures users are presented with clear and aesthetically pleasing error messages, maintaining a professional look even when something goes wrong.

<details>

<summary> Details </summary>

- **403 Forbidden**:
  - Displayed when a user attempts to access a restricted page or perform an unauthorized action.
  - Message: "Access Denied – You do not have permission to view this page."
  
- **404 Not Found**:
  - Displayed when a user tries to access a page that does not exist.
  - Message: "Oops! Page Not Found – The page you're looking for doesn't exist."

- **405 Method Not Allowed**:
  - Displayed when a user tries to perform an HTTP method that is not supported by the server for a specific URL.
  - Message: "Method Not Allowed – This action is not permitted."

- **500 Internal Server Error**:
  - Displayed when an unexpected error occurs on the server.
  - Message: "Something Went Wrong – Please try again later."

Each error page includes:
- A **consistent site layout** to keep users oriented.
- A **clear message** explaining the error.
- A **call-to-action link**, the "Go Back to Home" button, to help users navigate back to the main site.


- **403 Forbidden**
  ![403 Forbidden Screenshot](docs/images/features/errors/error-403.png)

- **404 Not Found**
  ![404 Not Found Screenshot](docs/images/features/errors/error-404.png)

- **405 Method Not Allowed**
  ![405 Method Not Allowed Screenshot]()

- **500 Internal Server Error**
  ![500 Internal Server Error Screenshot](docs/images/features/errors/500-server-error.png)

---

### Future Implementations

  I would add the following features:
  * Like/remove like from a recipe and view how many likes a recipe had received from other users
  * Recipe categorisation and tagging to facilitate a more comprehensive search and filter experience
  * An 'About' page to explain what the site is about and who it is for
  * Contact Form to make it easier for user's to contact the site admin
  * A share function for a user to share a recipe on social media
  * Users can add a recipe to a 'favourites' folder

---
  
## Project Management & Agile Methodologies

### Agile Development

This project was developed using Agile methodology which allowed me to iteratively and incrementally build my app, with flexibility to make changes to my design throughout the entire development process.

#### Kanban Board

GitHub Issues and Projects were used to manage the development process. Each part of the app is divided into Epics which are broken down into User Stories with Tasks. An Epic represents a large body of work, such as a feature. The board view of the Project feature was used to display and manage my progress in the form of a 'kanban board'. The user stories were added to the 'Todo' column to be prioritised for development, moved to the 'In Progress' column to indicate development of the feature had begun and finally moved to the 'Done' column when the feature had been implemented and the acceptance criteria had been met.

<details>

  <summary> Kanban Board  </summary>

  ![Kanban Board](docs/images/kanban-board-pp4.png)

</details>

[The Project Kanban Board](https://github.com/users/EJFleet/projects/2)

#### MoSCoW Prioritisation

User stories were prioritised using the MoSCoW prioritisation technique. Each user story was given one of the following labels:

- Must have - to indicate the user story is guaranteed to be delivered.
- Should have - to indicate the user story would add significant value but is not vital.
- Could have - to indicate the user story would have a small impact if left out.
- Won't have - to indicate the user story is not a priority in the current iteration.

---

## Technologies Used


  ### Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

  ### Frameworks, Libraries & Packages
  
- [Django 4.2.16](https://docs.djangoproject.com/en/4.2/) - The main web framework used to build the application, creating models, views and templates.
- [Bootstrap 5](https://getbootstrap.com/) - front-end CSS framework for modern responsiveness and pre-built components
- [Font Awesome 5.15.4](https://fontawesome.com/) - social media icons in footer
- [Google Fonts](https://fonts.google.com/) - fonts used on the app
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - enhanced form rendering with customizable styles and better integration with Bootstrap
- [cripsy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5) - Bootstrap 5 styling support to `django-crispy-forms`
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - user authentication, registration, and account management
- [Gunicorn](https://gunicorn.org/) - used for WSGI server
- [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL adapter for Python, used to interact with the PostgreSQL database
- [django-summernote](https://summernote.org/) - WYSIWYG text editor integrated into Django admin and forms for creating rich-text content
- [cloudinary 1.36.0](https://cloudinary.com/) - managing and serving images using the Cloudinary API
- [whitenoise (5.3.0)](https://whitenoise.readthedocs.io/en/latest/) - serving static files in production


### Tools

- [Git](https://git-scm.com/) - version control
- [GitHub](https://github.com/) - save and store the files for the app
- [GitPod](https://gitpod.io/) - developing the app
- [Heroku](https://heroku.com/) - deploying the app
- [PostgreSQL](https://www.postgresql.org/) - database
- [Cloudinary](https://cloudinary.com/) - storing images
- [Balsamiq](https://balsamiq.com/) - wireframes
- [Lucid.app](lucid.app) - creating the ERD
- [Coolors](https://coolors.co/) - colour scheme
- [Am I Responsive](https://ui.dev/amiresponsive) -responsive screenshots
- [favicon.io](https://favicon.io/) - custom favicon
- [FontAwesome](https://fontawesome.com/) - social media icons in footer
- [ChatGPT](https://chatgpt.com/) - debugging
- [The W3C Markup Validation Service](https://validator.w3.org/) - validating HTML
- [The W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - validating CSS
- [Code Insitute PEP8 Validator](https://pep8ci.herokuapp.com/#) - validating the Python code
- [JSHint](https://jshint.com/) - validating JavaScript
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
- [Codebeautify.org](https://codebeautify.org/python-formatter-beautifier) - formatting the code
- [Shields.io](https://shields.io/) - adding badges to the readme
- [Django Secret Key Generator](https://djecrety.ir/) - generating a secret key
- [Pexels](https://www.pexels.com/) - team member photos


##  Deployment & Local Development    

  
### Forking the GitHub Repository

  A copy of the original repository can be made through GitHub. Please follow the below steps to fork this repository.

  <details>
  <summary>Steps for forking GitHub Repository</summary>

  1. Navigate to GitHub and log in.  
  2. Once logged in, navigate to this repository using this link [My Cookbook Repository](https://github.com/EJFleet/pp4-my-cookbook-blog).
  3. Above the repository file section and to the top, right of the page is the '**Fork**' button, click on this to make a fork of this repository.
  4. You should now have access to a forked copy of this repository in your Github account.

  </details>

  -----

  ### Cloning the GitHub Repository

  A local clone of this repository can be made on GitHub. Please follow the below steps.

  <details>
  <summary>Steps for cloning GitHub Repository</summary>

  1. Navigate to GitHub and log in.
  2. The [My Cookbook Repository](https://github.com/EJFleet/pp4-my-cookbook-blog) can be found at this location.
  3. Above the repository file section, locate the '**Code**' button.
  4. Click on this button and choose your clone method from HTTPS, SSH or GitHub CLI, copy the URL to your clipboard by clicking the '**Copy**' button.
  5. Open your Git Bash Terminal.
  6. Change the current working directory to the location you want the cloned directory to be made.
  7. Type `git clone` and paste in the copied URL from step 4.
  8. Press '**Enter**' for the local clone to be created.

  For more details about forking and cloning a repository, please refer to [GitHub documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).


  </details> 

  ### Deploying to Heroku

  <details>

  <summary> Deploying to Heroku </summary>

  To get the Django framework installed and set up I followed the Code institutes [Django Blog cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)


  </details>

  
-----

## Testing

  ### Functionality

  Extensive testing was performed to ensure that the website ran correctly.

    #### Manual Testing

    ![Manual Testing Checklist]()


  ### Code Validation

  The code was validated using PEP8 standards to ensure readability and maintainability.

  <details>

  <summary> Validation for  </summary>

  ![ validation]()

  </details>

  <details>

  <summary> Validation for  </summary>

  ![ validation]()

  </details>

  <details>

  <summary> Validation for  </summary>

  ![ validation]()

  </details>


  ### Bug Fixes

  |Bug|Solution|Fixed?|
  |-----|-----|-----|
  | |  |  | 


  **There were no other known bugs at the time of submitting the project.**

## Credits

  ### Code Inspiration

  - 
  
    
  ### Acknowledgments

  * My mentor Brian Macharia for his help and clear explanations of what needed to be done
  * Lewis Dillon for facilitating our weekly standups and being a font of information and encouragement
  * My friends and family for testing the project on their devices and offering words of encouragement
  * My dog Po for making me take breaks from my desk