from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the TeamMember model.
    Includes support for Summernote fields.
    """
    list_display = ('name', 'jobtitle', 'location', 'status')
    search_fields = ['name']
    summernote_fields = ('bio',)
