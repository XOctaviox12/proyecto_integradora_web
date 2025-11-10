from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import  RegistroForm, ContactForm
from .models import Estadisticas, PageVisit, Jugadores, ComentarioContacto


CHARACTERS = [
    {"name": "Loya", "role": "Protagonista", "desc": "Alumno rebelde."},
    {"name": "Cendejas", "role": "Profesor", "desc": "Profesor malvado."},
]

CREATORS = [
    {"name": "Lenin", "role": "Diseño", "bio": "Concept art y UI."},
    {"name": "Octavio", "role": "Programación", "bio": "Gameplay."},
]

# def home(request):
#     history = "Face-Bomb combina humor, acción y nostalgia escolar en una experiencia tan absurda como divertida. Cada partida es una carrera contra el tiempo, la disciplina y el caos del aula.repárate para reír, esquivar y sobrevivir mientras los libros vuelan por tu cabeza y tus compañeros esperan ansiosos sus caramelos prohibidos."
#     return render(request, "inicio/home.html", {"history": history, "characters": CHARACTERS})
def home(request):
    # Incrementar contador de visitas
    visit, created = PageVisit.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()

    # Texto original
    history = (
        "Face-Bomb combina humor, acción y nostalgia escolar en una experiencia tan absurda como divertida. "
        "Cada partida es una carrera contra el tiempo, la disciplina y el caos del aula. "
        "Prepárate para reír, esquivar y sobrevivir mientras los libros vuelan por tu cabeza "
        "y tus compañeros esperan ansiosos sus caramelos prohibidos."
    )

    # Renderizar con todo el contexto
    return render(
        request,
        "inicio/home.html",
        {
            "history": history,
            "characters": CHARACTERS,
            "contador_visitas": visit.count,
        },
    )

def creators(request):
    return render(request, "inicio/creators.html", {"creators": CREATORS})

def contact(request):
    form = ContactForm(request.POST or None)
    sent = False

    if request.method == "POST" and form.is_valid():
        # Guardar el comentario
        ComentarioContacto.objects.create(
            nombre=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            mensaje=form.cleaned_data["message"]
        )

        # Mostrar mensaje de éxito
        sent = True
        messages.success(request, "¡Mensaje enviado correctamente!")
        form = ContactForm() 

    return render(request, "inicio/contact.html", {"form": form, "sent": sent})



def registro(request):
    # Contador de visitas
    visit, created = PageVisit.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()

    # Formulario de registro
    form = RegistroForm(request.POST or None)
    registrado = False

    if request.method == "POST" and form.is_valid():
        form.save()
        registrado = True
        form = RegistroForm() 

    # Contador de jugadores registrados
    contador_registros = Jugadores.objects.count()

    return render(request, 'inicio/registro.html', {
        'form': form,
        'registrado': registrado,
        'contador': contador_registros,
        'contador_visitas': visit.count
    })



