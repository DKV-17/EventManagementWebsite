from django.shortcuts import render
from events.models import Event
from testimonials.models import Testimonial

def home(request):

    events = Event.objects.order_by("-id")[:4]

    testimonials = Testimonial.objects.filter(
        is_approved=True
    ).order_by("-created_at")[:3]

    return render(request, "home/home.html", {
        "events": events,
        "testimonials": testimonials,
    })