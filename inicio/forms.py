from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)


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

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "⚠️ Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
