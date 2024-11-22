# Generated by Django 4.2.16 on 2024-11-22 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_teammember_status'),
        ('blog', '0010_recipe_team_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='team_member',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to='team.teammember'),
        ),
    ]
