# Generated by Django 4.1.5 on 2024-07-30 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_alter_scheduledetails_multi_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerPlatforms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('color', models.CharField(default='white', max_length=50)),
                ('status', models.CharField(default='active', max_length=50)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entityhascareer',
            name='platforms',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.careerplatforms'),
        ),
    ]