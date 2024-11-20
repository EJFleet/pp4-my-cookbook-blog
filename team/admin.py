from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(SummernoteModelAdmin):

    list_display = ('name', 'jobtitle', 'location', 'status',)
    search_fields = ['name']
    summernote_fields = ('bio',)