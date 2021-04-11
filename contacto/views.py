from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from proyectoweb.settings import EMAIL_HOST_USER
# Create your views here.


def contacto(request):
    if request.method == "POST":
        asunto = request.POST["asunto"]
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        mensaje = request.POST["mensaje"]
        recipient_list = ["topgambajrjdeveloper@gmail.com"]
        #cuerpo = EmailMessage("Mensaje desde la DevCordernadas", \
        #                     "El usuario con nombre {}, con asunto {} y la dirección de correo {} te escribe lo siguiente: \n\n {}".format(nombre, asunto, email, mensaje), "", ["tuemail@gmail.com"], reply_to=[email])

        send_mail(asunto, mensaje, EMAIL_HOST_USER, recipient_list)

        return render(request, "gracias.html")
    return render(request, "contacto.html")
