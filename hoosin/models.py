from django.db import models


class HoursEnrty(models.Model):
    professor = models.CharField()
    course = models.CharField()
    hours = models.CharField()
