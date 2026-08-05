from django.db import models

class Booking(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.full_name