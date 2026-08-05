from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    review = models.TextField()
    rating = models.IntegerField(default=5)
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name