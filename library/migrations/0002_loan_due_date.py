# Generated by Django 4.2 on 2025-06-20 10:22

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='due_date',
            field=models.DateField(default=library.models.get_due_date),
        ),
    ]
