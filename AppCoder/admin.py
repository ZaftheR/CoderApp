from django.contrib import admin
from .models import Curso, Profesor, Entregable, Estudiante, Perfil
# Register your models here.

admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(Perfil)