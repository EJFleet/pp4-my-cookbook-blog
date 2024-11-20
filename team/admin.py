from django.contrib import admin
from .models import TeamMember
from django_summernote.admin import SummernoteModelAdmin

@admin.register(TeamMember)
class TeamMemberAdmin(SummernoteModelAdmin):

    list_display = ('name', 'jobtitle', 'location')
    search_fields = ['name']
    summernote_fields = ('bio',)