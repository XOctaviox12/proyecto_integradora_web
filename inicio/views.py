from django.shortcuts import render
from .forms import ContactForm, RegistroForm
from django.contrib import messages

CHARACTERS = [
    {"name": "Astra", "role": "Protagonista", "desc": "Exploradora espacial."},
    {"name": "Kron", "role": "Antagonista", "desc": "Señor de las sombras."},
]

CREATORS = [
    {"name": "Evelyn", "role": "Diseño", "bio": "Concept art y UI."},
    {"name": "Juárez", "role": "Programación", "bio": "Gameplay."},
]


def home(request):
    history = "En 'Estrella Errante' controlas a Astra en una aventura espacial."
    return render(request, "inicio/home.html", {"history": history, "characters": CHARACTERS})


def creators(request):
    return render(request, "inicio/creators.html", {"creators": CREATORS})


def contact(request):
    form = ContactForm(request.POST or None)
    sent = False
    if request.method == "POST" and form.is_valid():
        sent = True
        form = ContactForm()
    return render(request, "inicio/contact.html", {"form": form, "sent": sent})


def registro(request):
    form = RegistroForm(request.POST or None)
    registrado = False

    if request.method == "POST":
        if form.is_valid():
            form.save()
            registrado = True
            messages.success(request, "🚀 Registro completado con éxito.")
            form = RegistroForm()  # limpiar formulario
        else:
            messages.error(request, "⚠️ Por favor corrige los errores antes de continuar.")

    return render(request, "inicio/registro.html", {"form": form, "registrado": registrado})
