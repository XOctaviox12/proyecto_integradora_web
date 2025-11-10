from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



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
        model = User
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
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("⚠️ Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    

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