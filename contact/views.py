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

        print("EMAIL_HOST_USER =", settings.EMAIL_HOST_USER)
        print("EMAIL_HOST_PASSWORD EXISTS =", bool(settings.EMAIL_HOST_PASSWORD))

        try:
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

            # Confirmation Email
            send_mail(
                subject="Thank You for Contacting Make Events",
                message=f"""
Dear {name},

Thank you for contacting Make Events.

We have received your enquiry successfully.

Regards,
Make Events Team
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

            messages.success(request, "Message sent successfully.")
            return redirect("contact")

        except Exception as e:
            print("SMTP ERROR:", repr(e))
            raise

    return render(request, "contact/contact.html")