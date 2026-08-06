from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        # Email to Admin
        send_mail(
            subject=f"New Contact Enquiry: {subject}",
            message=f"""
A new enquiry has been received.

Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        # Confirmation Email to User
        send_mail(
            subject="Thank You for Contacting Make Events",
            message=f"""
Dear {name},

Thank you for contacting Make Events.

We have received your enquiry successfully.

Our team will get back to you shortly.

Regards,
Make Events Team
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )
        messages.success(
    request,
    "Thank you for contacting Make Events. We have received your enquiry successfully. Our team will get back to you shortly."
)
        return redirect("contact")

    return render(request, "contact/contact.html")