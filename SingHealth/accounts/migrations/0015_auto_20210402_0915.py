# Generated by Django 3.1.7 on 2021-04-02 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_checklist_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffchecklistauthor', to='accounts.staff'),
        ),
        migrations.AlterField(
            model_name='checklist',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenantchecklistscore', to='accounts.tenant'),
        ),
        migrations.AlterField(
            model_name='checklistscore',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffwhoaudited', to='accounts.staff'),
        ),
        migrations.AlterField(
            model_name='checklistscore',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tenantaudited', to='accounts.tenant'),
        ),
    ]