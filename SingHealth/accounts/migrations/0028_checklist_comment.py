# Generated by Django 3.1.7 on 2021-04-05 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_remove_checklist_actual_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
