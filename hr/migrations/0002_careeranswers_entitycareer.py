# Generated by Django 5.1.1 on 2024-11-14 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='careeranswers',
            name='entitycareer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.entityhascareer'),
        ),
    ]