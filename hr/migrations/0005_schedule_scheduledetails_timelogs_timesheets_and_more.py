# Generated by Django 4.1.5 on 2024-07-11 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0004_remove_entities_address'),
        ('hr', '0004_alter_careerquestions_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_name', models.CharField(max_length=50)),
                ('monthly_hours', models.IntegerField()),
                ('break_duration', models.BigIntegerField()),
                ('schedule_type', models.CharField(max_length=50, null=True)),
                ('work_type', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(default='active', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('duration', models.IntegerField()),
                ('repeat', models.CharField(max_length=50)),
                ('days', models.CharField(max_length=50)),
                ('priority', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('amount_type', models.CharField(max_length=50)),
                ('other_type', models.CharField(max_length=50)),
                ('in_threshold', models.IntegerField()),
                ('out_threshold', models.IntegerField()),
                ('is_expandable', models.CharField(max_length=50)),
                ('must_check_in', models.SmallIntegerField()),
                ('must_check_out', models.SmallIntegerField()),
                ('timezone', models.CharField(max_length=50, null=True)),
                ('multi_day', models.CharField(default='false', max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.schedule')),
            ],
        ),
        migrations.CreateModel(
            name='TimeLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_area_code', models.CharField(max_length=50)),
                ('duration', models.BigIntegerField(null=True)),
                ('log_start', models.DateTimeField(null=True)),
                ('log_end', models.DateTimeField(null=True)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('log_type', models.CharField(max_length=50)),
                ('log_status', models.CharField(max_length=50)),
                ('timezone', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(default='active', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('period_start', models.DateTimeField(null=True)),
                ('period_end', models.DateTimeField(null=True)),
                ('scheduled_days', models.IntegerField(null=True)),
                ('scheduled_hours', models.IntegerField(null=True)),
                ('actual_days', models.IntegerField(null=True)),
                ('actual_hours', models.IntegerField(null=True)),
                ('approved_days', models.IntegerField(null=True)),
                ('approved_hours', models.IntegerField(null=True)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('prepared_by', models.CharField(default='SYSTEM', max_length=50)),
                ('approved_by', models.CharField(default='SYSTEM', max_length=50)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheetDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_type', models.CharField(default='regular', max_length=50)),
                ('schedule_status', models.CharField(default='ordinary', max_length=50)),
                ('actual_start', models.DateTimeField(null=True)),
                ('actual_end', models.DateTimeField(null=True)),
                ('approved_start', models.DateTimeField(null=True)),
                ('approved_end', models.DateTimeField(null=True)),
                ('total_hours', models.IntegerField(null=True)),
                ('confirmed_hours', models.IntegerField(null=True)),
                ('confirmation_type', models.CharField(max_length=50)),
                ('remarks', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(default='pending', max_length=50)),
                ('created_by', models.SmallIntegerField(default=0)),
                ('updated_by', models.SmallIntegerField(default=0)),
                ('deleted_by', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('log_end', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log_out', to='hr.timelogs')),
                ('log_start', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='log_in', to='hr.timelogs')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.schedule')),
                ('schedule_detials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.scheduledetails')),
                ('timesheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.timesheets')),
            ],
        ),
    ]