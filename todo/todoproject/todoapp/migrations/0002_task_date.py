# Generated by Django 4.2.4 on 2023-09-12 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-7-26'),
            preserve_default=False,
        ),
    ]
