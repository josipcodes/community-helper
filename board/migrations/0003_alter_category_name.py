# Generated by Django 3.2.23 on 2023-11-21 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('1', 'Helping the elderly'), ('2', 'Helping the youth'), ('3', 'Helping the people with disability'), ('4', 'Grocery run'), ('5', 'DIY, minor home improvements'), ('6', 'Urgent'), ('7', 'Other')], max_length=100),
        ),
    ]
