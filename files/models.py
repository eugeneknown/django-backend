from django.db import models
from entity.models import Entities

class Files(models.Model):
    hash = models.CharField(max_length=50)
    group_permission = models.CharField(max_length=50, null=True)
    file_path = models.TextField()
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField()
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)

    def hasfiles(self):
        hasfiles = EntityHasFiles.objects.get(files=self)


class EntityHasFiles(models.Model):
    files = models.ForeignKey(Files, on_delete=models.CASCADE)
    entity = models.ForeignKey(Entities, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="active")
    created_by = models.SmallIntegerField(default=0)
    updated_by = models.SmallIntegerField(default=0)
    deleted_by = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)