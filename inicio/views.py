from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import  RegistroForm, ContactForm
from .models import Estadisticas, PageVisit, Jugadores, ComentarioContacto
from django.templatetags.static import static


CHARACTERS = [
    {
        "name": "Loya",
        "role": "Protagonista",
        "desc": "Alumno rebelde que causa caos en clase.",
        "image": "images/loya.png"
    },
    {
        "name": "Cendejas",
        "role": "Profesor",
        "desc": "Profesor estricto que controla el salón.",
        "image": "images/cendejas.png"
    },
]

CREATORS = [
    {
        "name": "Lenin",
        "role": "Director de Arte & UI/UX",
        "bio": "Diseño visual, interfaces y coherencia estética entre plataformas.",
        "image": "images/lenin.jpg"
    },
    {
        "name": "Octavio",
        "role": "Líder de Programación",
        "bio": "Programación principal en Unity y soporte técnico entre plataformas.",
        "image": "images/octavio.jpg"
    },
    {
        "name": "Brandon",
        "role": "Artista 3D",
        "bio": "Modelado, texturas y optimización de assets para Unity.",
        "image": "images/brandon.jpg"
    },
    {
        "name": "Kevin",
        "role": "Animador",
        "bio": "Animación de personajes y efectos visuales.",
        "image": "images/kevin.jpg"
    },
    {
        "name": "Alan",
        "role": "Diseñador de Sonido",
        "bio": "Música, ambientación y efectos de sonido para el videojuego.",
        "image": "images/alan.jpg"
    },
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

    # ---- NUEVO: convertir imágenes a .url (sin mover nada más) ----
    characters_data = []
    for c in CHARACTERS:
        characters_data.append({
            **c,
            "image": type("Img", (), {"url": static(c["image"])})()
        })
    # ---------------------------------------------------------------

    # Renderizar con todo el contexto (igual que lo tenías)
    return render(
        request,
        "inicio/home.html",
        {
            "history": history,
            "characters": characters_data,   # aquí enviamos las imágenes ya listas
            "contador_visitas": visit.count,
        },
    )

def creators(request):
    creators_data = []
    for p in CREATORS:
        creators_data.append({
            **p,
            "image": type("Img", (), {"url": static(p["image"])})()
        })
    return render(request, "inicio/creators.html", {"creators": creators_data})

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



