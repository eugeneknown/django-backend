from django.db import models
from entity.models import Entities
from files.models import Files

# region careers

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


class CareerPlatforms(models.Model):
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
    platforms = models.ForeignKey(CareerPlatforms, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="active")
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class CareerQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    value = models.TextField()
    type = models.CharField(max_length=50)
    required = models.BooleanField(default=False)
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

# endregion  careers

# region schedule

class Schedule(models.Model):
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    schedule_name = models.CharField(max_length=50)
    monthly_hours = models.IntegerField()
    break_duration = models.BigIntegerField()
    schedule_type = models.CharField(max_length=50, null=True)
    work_type = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def scheduleDetails(self):
        scheduleDetails = ScheduleDetails.objects.get(schedule=self)


class ScheduleDetails(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='scheduleDetails')
    time_start = models.TimeField()
    time_end = models.TimeField()
    duration = models.IntegerField()
    repeat = models.CharField(max_length=50)
    days = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    amount = models.FloatField()
    amount_type = models.CharField(max_length=50)
    other_type = models.CharField(max_length=50)
    in_threshold = models.IntegerField()
    out_threshold = models.IntegerField()
    is_expandable = models.CharField(max_length=50)
    must_check_in = models.SmallIntegerField()
    must_check_out = models.SmallIntegerField()
    timezone = models.CharField(max_length=50, null=True)
    multi_day = models.CharField(max_length=50, default='False')
    status = models.CharField(max_length=50, default="pending")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


# endregion schedule

# region timesheet

class TimeSheets(models.Model):
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    month = models.IntegerField(null=True)
    period_start = models.DateTimeField(null=True)
    period_end = models.DateTimeField(null=True)
    scheduled_days = models.IntegerField(null=True)
    scheduled_hours = models.IntegerField(null=True)
    actual_days = models.IntegerField(null=True)
    actual_hours = models.IntegerField(null=True)
    approved_days = models.IntegerField(null=True)
    approved_hours = models.IntegerField(null=True)
    remarks = models.CharField(max_length=50, null=True)
    prepared_by = models.CharField(max_length=50, default="SYSTEM")
    approved_by =  models.CharField(max_length=50, default="SYSTEM")
    status = models.CharField(max_length=50, default="pending")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class TimeLogs(models.Model):
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    work_area_code =  models.CharField(max_length=50, default='WFH')
    duration = models.BigIntegerField(null=True)
    log_start = models.DateTimeField(null=True)
    log_end = models.DateTimeField(null=True)
    remarks =  models.CharField(max_length=50, null=True)
    log_type =  models.CharField(max_length=50, default='work')
    log_status =  models.CharField(max_length=50, default='unused')
    timezone =  models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


class TimeSheetDetails(models.Model):
    timesheet = models.ForeignKey(TimeSheets, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    schedule_detials = models.ForeignKey(ScheduleDetails, on_delete=models.CASCADE)
    log_start = models.ForeignKey(TimeLogs, on_delete=models.CASCADE, null=True, related_name='log_in')
    log_end = models.ForeignKey(TimeLogs, on_delete=models.CASCADE, null=True, related_name='log_out')
    schedule_type =  models.CharField(max_length=50, default='regular')
    schedule_status =  models.CharField(max_length=50, default='ordinary')
    actual_start = models.DateTimeField(null=True)
    actual_end = models.DateTimeField(null=True)
    approved_start = models.DateTimeField(null=True)
    approved_end = models.DateTimeField(null=True)
    total_hours = models.IntegerField(null=True)
    confirmed_hours = models.IntegerField(null=True)
    confirmation_type =  models.CharField(max_length=50)
    remarks =  models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, default="pending")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)


# endregion timesheet