from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.TeamMemberList.as_view(), name="team"),
    ]
