# Generated by Django 5.1.1 on 2024-11-12 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_entityreference'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencedetails',
            name='department',
            field=models.CharField(default='', max_length=50),
        ),
    ]
