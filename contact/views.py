from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages


def contact(request):

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        messages.success(
            request,
            "Thank you for contacting Make Events! Your enquiry has been submitted successfully. Our team will contact you soon."
        )

        return redirect("contact")

    return render(request, "contact/contact.html")