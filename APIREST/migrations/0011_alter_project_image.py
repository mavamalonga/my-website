# Generated by Django 4.0.5 on 2022-07-18 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIREST', '0010_rename_cvpdf_curriculumvitae_rename_skill_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='project'),
        ),
    ]