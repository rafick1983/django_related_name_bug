from django.db import models


class TheSameNamedModel(models.Model):
    name = models.CharField(max_length=10)
    buggy_m2m = models.ManyToManyField('app_a.SomeModel', related_name='+')
