from django.shortcuts import render
from django.views.generic import ListView
from .models import TeamMember


class TeamMemberList(ListView):
    """
    Display the Team Members page.

    This view displays all team members, split into 'owner'
    and 'team' categories,
    with pagination applied.
    """
    model = TeamMember
    template_name = 'team/team.html'
    paginate_by = 6
    context_object_name = 'team_members'

    def get_queryset(self):
        """
        Return all team members.
        """
        return TeamMember.objects.all()

    def get_context_data(self, **kwargs):
        """
        Add the owner and team members to the context.

        - 'owner': Team members with status=1.
        - 'team': Team members with status=0.
        - 'page_title': The title of the page.
        """
        context = super().get_context_data(**kwargs)
        context['owner'] = TeamMember.objects.filter(status=1)
        context['team'] = TeamMember.objects.filter(status=0)
        context['page_title'] = 'Meet the Team'
        return context
