from django.shortcuts import render
from django.views.generic import ListView
from .models import TeamMember


class TeamMemberList(ListView):

    """
    Display the Team Members page

    """
    model = TeamMember
    template_name = 'team/team.html'
    paginate_by = 6
    context_object_name = 'team_members'

    def get_context_data(self, **kwargs):

        """        
        Add the owner and team members to the context.        
        """
        context = super().get_context_data(**kwargs)
        context['owner'] = TeamMember.objects.filter(status=1),
        context['team'] = TeamMember.objects.filter(status=0),
        return context