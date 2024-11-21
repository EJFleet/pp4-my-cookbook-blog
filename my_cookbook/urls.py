from django.contrib import admin
from django.urls import path, include
from blog.views import MyCookbookLoginView, MyCookbookLogoutView, MyCookbookSignupView
from .views import handler404, handler500, handler403, handler405

urlpatterns = [
    path(
        '', include('blog.urls'), name='blog.urls'
        ),
    path(
        'accounts/login/', MyCookbookLoginView.as_view(),
        name='account_login'
        ),
    path(
        'accounts/logout/', MyCookbookLogoutView.as_view(),
        name='account_logout'
        ),
    path(
        'accounts/signup/', MyCookbookSignupView.as_view(),
        name='account_signup'
        ),
    path(
        'accounts/', include('allauth.urls')
        ),
    path(
        'summernote/', include('django_summernote.urls')
        ),
    path(
        'admin/', admin.site.urls
        ),
    path(
        'team/', include('team.urls'), name='team-urls'
        )
]

handler404 = 'my_cookbook.views.handler404'
handler500 = 'my_cookbook.views.handler500'
handler403 = 'my_cookbook.views.handler403'
handler405 = 'my_cookbook.views.handler405'
