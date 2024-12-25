from django import forms 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CursoFormulario(forms.ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el nombre"},),
            "comision": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el comision"})
        }
    
class EstudiantesFormulario(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el nombre"},),
            "apellido": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el apellido"},),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder":"Ingrese el email"})
        }
    
class ProfesoresFormulario(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el nombre"},),
            "apellido": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el apellido"},),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder":"Ingrese el email"})
        }
    

class EntregablesFormulario(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese el nombre"},),
            "fecha_de_entrega": forms.DateInput(attrs={"type": "date", "class": "form-conntrol"},),
            "entregado": forms.CheckboxInput(attrs={"class": "from-check-input", "type":"checkbox", "placeholder":"AAAA/MM/DD"})
        }



class UserUpdateForms(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ["first_name","last_name", "email"]


class UserProfileForms(forms.ModelForm):
    
    class Meta:
        model = Perfil
        fields = ["photo", "bio", "link"]