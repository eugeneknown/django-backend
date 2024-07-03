from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'

    def entities(self):
        entities = Entities.objects.get(users=self)


class Entities(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.OneToOneField(Users, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    middle_name = models.CharField(max_length=50, default="")
    permanent_address = models.TextField(default="")
    present_address = models.TextField(default="")
    image = models.TextField(null=True)
    email = models.EmailField(default="")
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True)
    contact_number = models.CharField(max_length=50)
    birthday = models.DateField(null=True)
    birth_place = models.CharField(max_length=50, default="")
    civil_status = models.CharField(max_length=50, default="")
    age = models.SmallIntegerField(null=True)
    gender = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class Client(models.Model):
   id = models.AutoField(primary_key=True)
   entity = models.ForeignKey(
       "Entities",
       on_delete=models.CASCADE,
    )
   client_type = models.CharField(max_length=50, default="")
   business_type = models.CharField(max_length=50, default="")
   timezone = models.CharField(max_length=50, default="")
   remarks = models.TextField(default="")
   onboard_date = models.DateField(default="")
   name = models.CharField(max_length=50, default="")
   status = models.CharField(max_length=50, default="")
   created_at = models.DateTimeField(null=True)
   updated_at = models.DateTimeField(null=True)
   deleted_at = models.DateTimeField(null=True)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(
        "Client",
        on_delete = models.CASCADE,
    )
    entity = models.ForeignKey(
        "Entities",
        on_delete = models.CASCADE,
    )
    department = models.CharField(max_length=50, default="")
    employee_type = models.CharField(max_length=50, default="")
    date_hired = models.DateField(null=True)
    date_resign = models.DateField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)