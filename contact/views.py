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
                subject="SMTP Test",
                message="SMTP Test",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Mail Sent!")

        except Exception as e:
            return render(
                request,
                "contact/contact.html",
                {
                    "smtp_error": str(e)
                }
            )

        return redirect("contact")

    return render(request, "contact/contact.html")