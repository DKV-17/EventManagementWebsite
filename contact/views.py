from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message,
        )

        try:
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

            messages.success(request, "Contact saved and email sent successfully!")

        except Exception as e:
            messages.error(request, f"SMTP Error: {e}")

        return redirect("contact")

    return render(request, "contact/contact.html")