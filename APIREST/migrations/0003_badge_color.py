# Generated by Django 4.0.5 on 2022-07-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIREST', '0002_remove_project_badges_remove_project_skills_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='badge',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
    ]