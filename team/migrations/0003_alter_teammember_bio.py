# Generated by Django 4.2.16 on 2024-11-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_teammember_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='bio',
            field=models.TextField(default='A wonderul team member!', max_length=1000),
        ),
    ]
