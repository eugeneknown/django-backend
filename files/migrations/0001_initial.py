# Generated by Django 5.1.1 on 2024-11-05 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash', models.CharField(max_length=50)),
                ('group_permission', models.CharField(max_length=50, null=True)),
                ('file_path', models.TextField()),
                ('file_type', models.CharField(max_length=100)),
                ('file_size', models.IntegerField()),
                ('status', models.CharField(default='active', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityHasFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='active', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities')),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.files')),
            ],
        ),
    ]
