from django.db import models


class UtilityBody(models.Model):
    service_name = models.CharField(max_length=30)

