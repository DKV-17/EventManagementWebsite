from django.shortcuts import render, get_object_or_404
from .models import Event

def events(request):
    events = Event.objects.all()
    return render(request, 'events/events.html', {
        'events': events
    })

def event_details(request, id):
    event = get_object_or_404(Event, id=id)

    return render(request, 'events/event_details.html', {
        'event': event
    })