from django.db import models
from entity.models import Entities
from files.models import Files

class Careers(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    benifits = models.TextField()
    pay_types = models.TextField()
    experience = models.TextField()
    descriptions = models.TextField()
    qualifications = models.TextField()
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def hasquestions(self):
        hasquestions = CareerHasQuestions.objects.get(careers=self)
    

class CareerTags(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    color = models.CharField(max_length=50, default="white")
    status = models.CharField(max_length=50, default="active")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class EntityHasCareer(models.Model):
    id = models.AutoField(primary_key=True)
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    careers = models.ForeignKey(Careers, on_delete=models.CASCADE)
    tags = models.ForeignKey(CareerTags, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="active")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class CareerQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    value = models.TextField()
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def hasquestions(self):
        hasquestions = CareerHasQuestions.objects.get(questions=self)


class CareerHasQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    careers = models.ForeignKey(Careers, on_delete=models.CASCADE, related_name="hasquestions")
    questions = models.ForeignKey(CareerQuestions, on_delete=models.CASCADE, related_name="hasquestions")
    order = models.IntegerField(default=0)
    section = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class CareerAnswers(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(CareerQuestions, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    files = models.ForeignKey(Files, on_delete=models.CASCADE, null=True)
    value = models.TextField()
    status = models.CharField(max_length=50, default="active")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)