# Generated by Django 4.0.5 on 2022-07-07 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIREST', '0006_remove_customer_firstname_remove_customer_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
