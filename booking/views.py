from django.shortcuts import render, redirect
from .models import Booking

def booking(request):

    if request.method == "POST":

        Booking.objects.create(

            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            event_type=request.POST.get("event_type"),
            event_date=request.POST.get("event_date"),
            location=request.POST.get("location"),
            message=request.POST.get("message")

        )

        return redirect("booking")

    event = request.GET.get("event", "")

    return render(
        request,
        "booking/booking.html",
        {
            "event": event
        }
    )