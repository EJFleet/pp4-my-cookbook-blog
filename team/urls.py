from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TeamMemberList.as_view(), name="team"),
    ]
