# Generated by Django 4.2.16 on 2024-11-25 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_recipe_description_alter_recipe_ingredients_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='updated_on',
        ),
    ]