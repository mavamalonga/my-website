# Generated by Django 4.0.5 on 2022-07-06 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIREST', '0003_badge_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pdf', models.FileField(upload_to='pdf')),
            ],
        ),
    ]