from django import forms
from django.core.exceptions import ValidationError
from .models import Jugadores
from game_site.firebase import db   

class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "cosmic-input",
            "placeholder": "••••••••"
        })
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "cosmic-input",
            "placeholder": "Repite tu contraseña"
        })
    )

    class Meta:
        model = Jugadores
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "cosmic-input",
                "placeholder": "Nombre de usuario"
            }),
            "email": forms.EmailInput(attrs={
                "class": "cosmic-input",
                "placeholder": "correo@galaxia.com"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise ValidationError("⚠️ Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        jugador = super().save(commit=False)
        jugador.password = self.cleaned_data["password1"]

        if commit:
            jugador.save()

            # GUARDAR TAMBIÉN EN FIRESTORE
            db.collection("jugadores").document(jugador.username).set({
                "username": jugador.username,
                "email": jugador.email,
                "password": jugador.password,  # si quieres, quítalo
            })

        return jugador


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            "type": "text",
            "class": "cosmic-input",
            "placeholder": "Escribe tu nombre completo",
            "id": "id_name",
            "autocomplete": "off"
        })
    )

    email = forms.EmailField(
        label="Correo Electrónico",
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "cosmic-input",
            "placeholder": "tu@correo.com",
            "id": "id_email"
        })
    )

    message = forms.CharField(
        label="Mensaje",
        required=True,
        widget=forms.Textarea(attrs={
            "class": "cosmic-input",
            "rows": 4,
            "placeholder": "Tu mensaje intergaláctico...",
            "id": "id_message"
        })
    )
