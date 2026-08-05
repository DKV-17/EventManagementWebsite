from django.db import models

class Event(models.Model):
    EVENT_TYPES = [
        ("Conference", "Conference"),
        ("Corporate", "Corporate"),
        ("Wedding", "Wedding"),
        ("Birthday", "Birthday"),
        ("Festival", "Festival"),
        ("Exhibition", "Exhibition"),
        ("Private Party", "Private Party"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=EVENT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to="events/")
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title