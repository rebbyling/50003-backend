# Generated by Django 3.1.7 on 2021-04-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20210404_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='actual_img',
        ),
    ]