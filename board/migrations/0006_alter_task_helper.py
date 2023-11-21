# Generated by Django 3.2.23 on 2023-11-21 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0005_alter_task_final_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='helper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helper', to=settings.AUTH_USER_MODEL),
        ),
    ]
