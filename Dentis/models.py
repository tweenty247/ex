from django.db import models


class AppointmentForm(models.Model):
    your_name = models.CharField(max_length=255, null=True, blank=True)
    your_phone = models.IntegerField(null=True, blank=True)
    your_email = models.EmailField()
    your_address = models.CharField(max_length=255, null=True, blank=True)
    your_scheldule = models.CharField(max_length=255, null=True, blank=True)
    your_time = models.CharField(max_length=255, null=True, blank=True)
    your_message = models.TextField()

    def __str__(self):
        return self.your_name

