from django import forms
from .models import Explorador
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)
    email = forms.EmailField(label="Correo")
    message = forms.CharField(label="Mensaje", widget=forms.Textarea)


class RegistroForm(forms.ModelForm):
    contraseña1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control cosmic-input",
            "placeholder": "••••••••"
        })
    )
    contraseña2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control cosmic-input",
            "placeholder": "Repite tu contraseña"
        })
    )

    class Meta:
        model = Explorador
        fields = ["nombre", "correo"]
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control cosmic-input",
                "placeholder": "Nombre completo"
            }),
            "correo": forms.EmailInput(attrs={
                "class": "form-control cosmic-input",
                "placeholder": "correo@galaxia.com"
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("contraseña1")
        p2 = cleaned_data.get("contraseña2")
        if p1 and p2 and p1 != p2:
            raise ValidationError("⚠️ Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        explorador = super().save(commit=False)
        explorador.contraseña = self.cleaned_data["contraseña1"]
        if commit:
            explorador.save()
        return explorador
