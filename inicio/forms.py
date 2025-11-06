from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# --- Formulario de contacto (ya lo tenías) ---
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)

# --- Formulario de registro nuevo ---
class RegistroForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control cosmic-input",
            "placeholder": "••••••••"
        })
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control cosmic-input",
            "placeholder": "Repite tu contraseña"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control cosmic-input",
                "placeholder": "Nombre de usuario"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control cosmic-input",
                "placeholder": "correo@galaxia.com"
            }),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("⚠️ Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user