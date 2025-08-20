from django import forms
from django.contrib.auth import get_user_model
from .models import Cliente

User = get_user_model()

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'role']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if user.role != 'CLIENT':  # Forzamos a que siempre sea CLIENT
            user.role = 'CLIENT'
        if commit:
            user.save()
        return user


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'ci', 'nombre', 'apellido_p', 'apellido_m',
            'telefono_principal', 'telefono_secundario',
            'direccion_principal', 'direccion_secundaria', 'email'
        ]
