from django.db import models

# Create your models here.

class emissions(models.Model):
    Id = models.AutoField(primary_key=True)
    Date_Created = models.DateField()
    Accounting_Period = models.CharField(max_length=255)
    Scope_1 = models.IntegerField(null=True, blank=True)
    Scope_2 = models.IntegerField(null=True, blank=True)
    Scope_3 = models.IntegerField(null=True, blank=True)