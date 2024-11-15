# Generated by Django 5.1.1 on 2024-11-05 13:46

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_type', models.CharField(default='', max_length=50)),
                ('business_type', models.CharField(default='', max_length=50)),
                ('timezone', models.CharField(default='', max_length=50)),
                ('remarks', models.TextField(default='')),
                ('onboard_date', models.DateField(default='')),
                ('name', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Entities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='', max_length=50)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('middle_name', models.CharField(default='', max_length=50)),
                ('nickname', models.CharField(default='', max_length=50)),
                ('children', models.SmallIntegerField(null=True)),
                ('permanent_address', models.TextField(default='')),
                ('present_address', models.TextField(default='')),
                ('image', models.TextField(null=True)),
                ('email', models.EmailField(default='', max_length=254)),
                ('email_verified', models.BooleanField(default=False)),
                ('email_verified_at', models.DateTimeField(null=True)),
                ('contact_number', models.CharField(max_length=50)),
                ('alternative_number', models.CharField(max_length=50, null=True)),
                ('birthday', models.DateField(null=True)),
                ('birth_order', models.SmallIntegerField(null=True)),
                ('birth_place', models.CharField(default='', max_length=50)),
                ('civil_status', models.CharField(default='', max_length=50)),
                ('age', models.SmallIntegerField(null=True)),
                ('gender', models.CharField(default='', max_length=50)),
                ('education', models.CharField(default='', max_length=50)),
                ('course', models.CharField(default='', max_length=50)),
                ('status', models.CharField(default='active', max_length=50)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('users', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(default='', max_length=50)),
                ('employee_type', models.CharField(default='', max_length=50)),
                ('date_hired', models.DateField(null=True)),
                ('date_resign', models.DateField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.client')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities'),
        ),
        migrations.CreateModel(
            name='EntityDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('salary', models.CharField(default='', max_length=50)),
                ('us_time', models.CharField(default='', max_length=50)),
                ('work_in_office', models.CharField(default='', max_length=50)),
                ('transpo', models.CharField(default='', max_length=50)),
                ('application', models.CharField(default='', max_length=50)),
                ('start', models.CharField(default='', max_length=50)),
                ('condition', models.CharField(default='', max_length=50)),
                ('part_time', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='entity.entities')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total_experience', models.CharField(default='', max_length=50)),
                ('other_experience', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entity.entities')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(default='', max_length=50)),
                ('position_held', models.CharField(default='', max_length=50)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('handled', models.CharField(default='', max_length=50)),
                ('stay_length', models.CharField(default='', max_length=50)),
                ('leave_reason', models.CharField(default='', max_length=50)),
                ('salary', models.CharField(default='', max_length=50)),
                ('present', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='entity.experience')),
            ],
        ),
    ]
