
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Curso, Profesor, Entregable, Estudiante, Perfil
from .forms import CursoFormulario, EstudiantesFormulario, ProfesoresFormulario, EntregablesFormulario, UserUpdateForms, UserProfileForms


@login_required
def ver_perfil(request):
    return render(request, 'AppCoder/ver-perfil.html') #Es el renderizado para las templates de la seccion Perfil

@login_required
def editar_perfil(request):
    
    perfil, _ = Perfil.objects.get_or_create(usuario=request.user)
    perfil_form = UserProfileForms(request.POST, request.FILES, instance=perfil)
    
    if request.method == 'POST':
        form = UserUpdateForms(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            perfil_form.save()
            return redirect('ver-perfil') 
    else: 
        form = UserUpdateForms(instance=request.user)
        perfil_form = UserProfileForms(instance=perfil)
    return render(request, 'AppCoder/forms/editar-perfil.html', {"form":form ,"perfil_form":perfil_form}) #Es el renderizado para las templates de la seccion Perfil

@login_required
def editar_contraseña(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('ver-perfil')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'AppCoder/forms/editar-contraseña.html', {"form":form})


def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['contraseña']
        user = authenticate(request, username=usuario, password=contraseña)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {usuario}')
            return redirect('inicio') # Redirige a la página de inicio o donde quieras 
        else: return render(request, 'AppCoder/forms/iniciar_sesion.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, "AppCoder/forms/iniciar_sesion.html")

def cerrar_sesion(request):
        logout(request)
        messages.success(request, f'Sesión cerrada exitosamente')
        return redirect('iniciar-sesion')


def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar-sesion')
    else:
        form = UserCreationForm()
    return render(request, 'AppCoder/forms/registrar_usuario.html', {'form': form})



def curso(request):
    
    query = request.GET.get('q')
    if query:
        curso =  Curso.objects.filter(nombre__icontains=query) | Curso.objects.filter(comision__icontains=query)
    else:
        curso = Curso.objects.all() #Esto se obtienen los atributos completos de la clase
    return render(request, 'AppCoder/cursos.html', {'cursos':curso})#Es el renderizado para las templates de la seccion Curso

def inicio(request):
    return render(request, 'AppCoder/index.html') #Es el renderizado para las templates de la seccion Inicio


@login_required
def profesor(request):
    profesor = Profesor.objects.all() #Esto se obtienen los atributos completos de la clase
    print(profesor)
    
    return render(request, 'AppCoder/profesores.html', {'profesor':profesor}) #Es el renderizado para las templates de la seccion profesores

@login_required
def estudiante(request):
    estudiante = Estudiante.objects.all() #Esto se obtienen los atributos completos de la clase
    print(estudiante)
    
    return render(request, 'AppCoder/estudiantes.html', {'estudiante':estudiante}) #Es el renderizado para las templates de la seccion estudiantes

@login_required
def entregable(request):    
    entregable = Entregable.objects.all() #Esto se obtienen los atributos completos de la clase
    print(entregable)
    
    return render(request, 'AppCoder/entregables.html', {'entregable':entregable}) #Es el renderizado para las templates de la seccion entregables


#-----Funciones para ingresar informacion a la BD -----

@login_required
def formulario_curso_api(request):
    
    if request.method == "POST":
        curso_form = CursoFormulario(request.POST)
        
        if curso_form.is_valid():
            info_limpia = curso_form.cleaned_data
            curso = Curso(nombre=info_limpia["nombre"], comision=info_limpia["comision"])
            curso.save()
            return redirect("cursos")
    else:
        curso_form = CursoFormulario()
    
    return render(request, 'AppCoder/forms/curso-formulario.html', {"form": curso_form})

@login_required
def formulario_estudiantes_api(request):
    
    if request.method == "POST":
        estudiantes_form = EstudiantesFormulario(request.POST)
        
        if estudiantes_form.is_valid():
            info_limpia = estudiantes_form.cleaned_data
            estudiantes = Estudiante(nombre=info_limpia["nombre"], apellido=info_limpia["apellido"], email=info_limpia["email"])
            estudiantes.save()
            return redirect("estudiantes-formulario")
    else:
        estudiantes_form = EstudiantesFormulario()
    
    return render(request, 'AppCoder/forms/estudiante-formulario.html', {"form": estudiantes_form})

@login_required
def formulario_profesores_api(request):
    
    if request.method == "POST":
        profesores_form = ProfesoresFormulario(request.POST)
        
        if profesores_form.is_valid():
            profesores_form.save()
            return redirect("profesores")
    else:
        profesores_form = ProfesoresFormulario()
    
    return render(request, 'AppCoder/forms/profesores-formulario.html', {"form":profesores_form})


@login_required
def formulario_entregrables_api(request):
    
    if request.method == "POST":
        entregables_form = EntregablesFormulario(request.POST)
        
        if entregables_form.is_valid():
            info_limpia = entregables_form.cleaned_data
            entregables = Entregable(nombre=info_limpia["nombre"], fechaDeEntrega=info_limpia["fechaDeEntrega"], entregado=info_limpia["entregado"])
            entregables.save()
            return redirect("entregables")
    else:
        entregables_form = EntregablesFormulario()
    
    return render(request, 'AppCoder/forms/entregables-formulario.html', {"form": entregables_form})



#-----Funciones para eliminar informacion a la BD -----


def eliminar_profesor(request, id):

    profesor = Profesor.objects.get(id=id)
    profesor.delete()
    return redirect("profesores")

def eliminar_curso(request, id):

    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect("cursos")

def eliminar_estudiante(request, id):

    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect("estudiantes")

def eliminar_entregable(request, id):

    entregable = Entregable.objects.get(id=id)
    entregable.delete()
    return redirect("entregables")


#-----Funciones para eliminar informacion a la BD -----


def editar_profesor(request, id):
    
    profesor = Profesor.objects.get(id=id)
    
    if request.method == "POST":
        profesores_form = ProfesoresFormulario(request.POST)
        if profesores_form.is_valid():
            info_limpia = profesores_form.cleaned_data
            profesor.nombre = info_limpia["nombre"]
            profesor.apellido= info_limpia["apellido"]
            profesor.email = info_limpia["email"]
            profesor.profesion = info_limpia["profesion"]
            profesor.save()
        return redirect("profesores")
    else:
        profesores_form = ProfesoresFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
    
    return render(request, "AppCoder/editar-profesor.html", {"form":profesores_form})




"""------------------------------------Generar visatas de clases------------------------------------""" 
#Para algun proyecto usar vistas con funciones o vistas de clases, no usar los dos 

#clases para ver informacion
class CursoListview(ListView):
    model = Curso
    context_object_name = "cursos"
    template_name = "AppCoder/vbc/cursos-vbc.html"



#Clases para crear informacion
class CursoCreateView(CreateView):
    model = Curso
    template_name = "AppCoder/vbc/cusros-vbc-crea.html"
    fields = ["nombre", "comision"]
    success_url = reverse_lazy("cursos-vbc")


#Clases para eliminar informacion
class CursoDeleteView(DeleteView):
    model = Curso
    template_name = "AppCoder/vbc/cusros-vbc-eliminar.html"
    success_url = reverse_lazy("cursos-vbc")


#Clases para editar informacion
class CursoUpdateView(UpdateView):
    model = Curso
    template_name = "AppCoder/vbc/cursos-vbc-editar.html"
    fields = "__all__"
    success_url = reverse_lazy("cursos-vbc")