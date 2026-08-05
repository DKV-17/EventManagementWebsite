from django.shortcuts import render, get_object_or_404
from .models import Event


def event_details(request, id):
    event = get_object_or_404(Event, id=id)

    return render(request, "events/event_details.html", {
        "event": event
    })

def events(request):
    events = Event.objects.all()

    category = request.GET.get("category")
    location = request.GET.get("location")

    if category:
        events = events.filter(category=category)

    if location:
        events = events.filter(location=location)

    context = {
        "events": events,
        "categories": Event.EVENT_TYPES,
        "locations": [
            "Chennai",
            "Coimbatore",
            "Madurai",
            "Salem",
            "Trichy",
            "Erode",
            "Tirunelveli",
            "Vellore",
            "Pondicherry",
            "Bangalore",
        ]
    }

    return render(request, "events/events.html", context)