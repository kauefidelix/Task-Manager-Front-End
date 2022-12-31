from django.db import models
import uuid

# Create your models here.

class Card(models.Model):
    card_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=264, unique=False)
    content = models.TextField(null=True, blank=True)
    creation_date = models.DateField()
    last_modified = models.DateField()
    column = models.CharField(max_length=264, unique=False)
    assignee = models.CharField(max_length=264, unique=False, null=True, blank=True)
    card_type = models.CharField(max_length=264, unique=False)
    epic_link = models.ForeignKey('Epic', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return str(self.card_id)

class Epic(models.Model):
    epic_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=264, unique=True)
    content = models.TextField(null=True, blank=True)
    creation_date = models.DateField()
    last_modified = models.DateField()
    assignee = models.CharField(max_length=264, unique=False, null=True, blank=True)
    def __str__(self):
        return str(self.name)
