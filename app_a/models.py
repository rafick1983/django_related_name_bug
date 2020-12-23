from django.db import models


class SomeModel(models.Model):
    name = models.CharField(max_length=10)


class TheSameNamedModel(models.Model):
    name = models.CharField(max_length=10)
    buggy_m2m = models.ManyToManyField(SomeModel, related_name='+')
