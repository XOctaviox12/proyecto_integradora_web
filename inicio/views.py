from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import  RegistroForm, ContactForm
from .models import Estadisticas, PageVisit


CHARACTERS = [
    {"name": "Loya", "role": "Protagonista", "desc": "Alumno rebelde."},
    {"name": "Cendejas", "role": "Profesor", "desc": "Profesor malvado."},
]

CREATORS = [
    {"name": "Lenin", "role": "Diseño", "bio": "Concept art y UI."},
    {"name": "Octavio", "role": "Programación", "bio": "Gameplay."},
]

def home(request):
    history = "Face-Bomb combina humor, acción y nostalgia escolar en una experiencia tan absurda como divertida. Cada partida es una carrera contra el tiempo, la disciplina y el caos del aula.repárate para reír, esquivar y sobrevivir mientras los libros vuelan por tu cabeza y tus compañeros esperan ansiosos sus caramelos prohibidos."
    return render(request, "inicio/home.html", {"history": history, "characters": CHARACTERS})

def creators(request):
    return render(request, "inicio/creators.html", {"creators": CREATORS})

def contact(request):
    form = ContactForm(request.POST or None)
    sent = False
    if request.method == "POST" and form.is_valid():
        sent = True
        messages.success(request, "¡Mensaje enviado correctamente! 🚀")
        form = ContactForm()  # Limpia el formulario
    return render(request, "inicio/contact.html", {"form": form, "sent": sent})

# 🪐 Vista de registro con contador

def registro(request):
    # Contador de visitas
    visit, created = PageVisit.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()

    # Contador de usuarios registrados (usa el modelo User)
    contador_registros = User.objects.count()

    return render(request, 'inicio/registro.html', {
        'contador_registros': contador_registros,
        'contador_visitas': visit.count
    })




