# Generated by Django 3.1.7 on 2021-04-02 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210402_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='accounts.tenant'),
        ),
    ]
