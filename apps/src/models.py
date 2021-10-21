from django.db import models


class Base(models.Model):
    date = models.CharField(max_length=255)
    open = models.CharField(max_length=255)
    high = models.CharField(max_length=255)
    low = models.CharField(max_length=255)
    close = models.CharField(max_length=255)
    adj_close = models.CharField(max_length=255)
    volume = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} -- {self.date}"
