from django.shortcuts import render
from .forms import ContactForm
from .forms import ContactForm, RegistroForm 

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
        sent = True  # en un caso real se guardaría en BD o mandaría correo
        form = ContactForm()
    return render(request, "inicio/contact.html", {"form": form, "sent": sent})


# 👉 Nueva vista para la página de registro
def registro(request):
    return render(request, "inicio/registro.html")
