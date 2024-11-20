from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail, EmailMessage


class Users(AbstractUser):
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'

    def entities(self):
        entities = Entities.objects.get(users=self)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    # the below like concatinates your websites reset password url and the reset email token which will be required at a later stage
    email_plaintext_message = "Open the link to reset your password" + " " + "{}?token={}".format(instance.request.build_absolute_uri("http://localhost:3100/authentication/change-password"), reset_password_token.key)
    
    """
        this below line is the django default sending email function, 
        takes up some parameter (title(email title), message(email body), from(email sender), to(recipient(s))
    """
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Crediation portal account"),
        # message:
        email_plaintext_message,
        # from:
        "systems@eighty20virtual.com",
        # to:
        ["systems@eighty20virtual.com"],
        # [reset_password_token.user.email],
        fail_silently=False,
    )


class Entities(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.OneToOneField(Users, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    middle_name = models.CharField(max_length=50, default="")
    nickname = models.CharField(max_length=50, default="")
    children = models.CharField(max_length=50, null=True)
    permanent_address = models.TextField(default="")
    present_address = models.TextField(default="")
    image = models.TextField(null=True)
    email = models.EmailField(default="")
    email_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(null=True)
    contact_number = models.CharField(max_length=50)
    alternative_number = models.CharField(max_length=50, null=True)
    birthday = models.DateField(null=True)
    birth_order = models.SmallIntegerField(null=True)
    birth_place = models.CharField(max_length=50, default="")
    civil_status = models.CharField(max_length=50, default="")
    age = models.SmallIntegerField(null=True)
    gender = models.CharField(max_length=50, default="")
    education = models.CharField(max_length=50, default="")
    course = models.CharField(max_length=50, default="")
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def details(self):
        details = EntityDetails.objects.get(entity=self)

    def reference(self):
        reference = EntityReference.objects.get(entity=self)


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(
        Entities,
        on_delete=models.CASCADE,
    )
    total_experience = models.CharField(max_length=50, default="")
    other_experience = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def details(self):
        details = ExperienceDetails.objects.get(experience=self)


class ExperienceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name='details',
    )
    company = models.CharField(max_length=50, default="")
    department = models.CharField(max_length=50, default="")
    position_held = models.CharField(max_length=50, default="")
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    handled = models.CharField(max_length=50, default="")
    stay_length = models.CharField(max_length=50, default="")
    leave_reason = models.CharField(max_length=50, default="")
    salary = models.CharField(max_length=50, default="")
    present = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class EntityDetails(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(
        Entities,
        on_delete=models.CASCADE,
        related_name='details',
    )
    salary = models.CharField(max_length=50, default="")
    us_time = models.CharField(max_length=50, default="")
    work_in_office = models.CharField(max_length=50, default="")
    transpo = models.CharField(max_length=50, default="")
    application = models.CharField(max_length=50, default="")
    start = models.CharField(max_length=50, default="")
    condition = models.CharField(max_length=50, default="")
    part_time = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class EntityReference(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(
        Entities,
        on_delete=models.CASCADE,
        related_name='reference',
    )
    name = models.CharField(max_length=50, default="")
    position = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    contact_number = models.CharField(max_length=50, default="")
    company = models.CharField(max_length=50, default="")
    company_email = models.EmailField(default="")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(
        Entities,
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
        Client,
        on_delete = models.CASCADE,
    )
    entity = models.ForeignKey(
        Entities,
        on_delete = models.CASCADE,
    )
    department = models.CharField(max_length=50, default="")
    employee_type = models.CharField(max_length=50, default="")
    date_hired = models.DateField(null=True)
    date_resign = models.DateField(null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)