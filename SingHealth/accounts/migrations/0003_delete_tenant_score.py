# Generated by Django 3.1.7 on 2021-04-21 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_image_date_added'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tenant_score',
        ),
    ]
