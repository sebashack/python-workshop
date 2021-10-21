from django.shortcuts import render


def contactForm(request):
    return render(request, "contactForm.html")
