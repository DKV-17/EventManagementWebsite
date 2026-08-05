from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestimonialForm

def testimonial(request):

    if request.method == "POST":

        form = TestimonialForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Thank you! Your review has been submitted and is awaiting admin approval."
            )

            return redirect("testimonial")

    else:
        form = TestimonialForm()

    return render(
        request,
        "testimonials/testimonial_form.html",
        {
            "form": form
        }
    )