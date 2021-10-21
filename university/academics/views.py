from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def contactForm(request):
    return render(request, "contactForm.html")


def contact(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["sebastian.pld.g@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactSuccess.html")
    return render(request, "contactForm.html")
