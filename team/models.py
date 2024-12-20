from django.db import models
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Team Member"),
    (1, "Owner"),
)


class TeamMember(models.Model):
    """
    A model to create profiles for team members.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    bio = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        default="A wonderful team member!"
    )
    jobtitle = models.CharField(max_length=50, verbose_name='Job Title')
    status = models.IntegerField(choices=STATUS, default=0)
    location = models.CharField(max_length=60)
    headshot = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
