from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_team_members(request):
    return HttpResponse('This works!')
