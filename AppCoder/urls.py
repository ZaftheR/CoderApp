from AppCoder import views
from django.urls import path

urlpatterns = [
    
    #----funciones para mostrar perfiles, editar perdiles y cambiar contraseñas----
    path('ver-perfil/', views.ver_perfil, name="ver-perfil"),
    path('editar-perfil/', views.editar_perfil, name="editar-perfil"),
    path('editar-contraseña/', views.editar_contraseña, name="editar-contraseña"),
    
    #----funciones para registro, iniciar y cerrar sesion----
    path('iniciar_sesion/', views.iniciar_sesion, name="iniciar-sesion"),
    path('cerrar_sesion/', views.cerrar_sesion, name="cerrar-sesion"),
    path('registrar_usuario/', views.registrar_usuario, name="registrar-usuario"),
    
    #----funciones para ver informacion----
    path('curso/', views.curso, name='cursos'),
    path('', views.inicio, name= 'inicio'),
    path('profesores/', views.profesor, name= 'profesores'),
    path('estudiantes/', views.estudiante, name= 'estudiantes'),
    path('entregables/', views.entregable, name= 'entregables'),
    
    #----formularios para agregar información----
    path('curso-formulario/', views.formulario_curso_api, name= 'curso-formulario'),
    path('estudiantes-formulario/', views.formulario_estudiantes_api, name= 'estudiantes-formulario'),
    path('profesores-formulario/', views.formulario_profesores_api, name= 'profesores-formulario'),
    path('entregables-formulario/', views.formulario_entregrables_api, name= 'entregables-formulario'),
    
    #----funciones para eliminar informacion----
    path('profesor-eliminar/<int:id>', views.eliminar_profesor, name= 'profesor-eliminar'),
    path('curso-eliminar/<int:id>', views.eliminar_curso, name='curso-eliminar'),
    path('estudiante-eliminar/<int:id>', views.eliminar_estudiante, name= 'estudiante-eliminar'),
    path('entregable-eliminar/<int:id>', views.eliminar_entregable, name= 'entregable-eliminar'),
    
    #----funciones para editar informacion----
    path('profesor-editar/<int:id>', views.editar_profesor, name= 'profesor-editar'),
    
    #------------------------funciones para vistas por clases---------------------------------------------
    
    #----clases para ver informacion----
    path("cursos-vbc/", views.CursoListview.as_view(), name = "cursos-vbc"),
    
    #----Clases para crear informacion----
    path("cursos-vbc/crear", views.CursoCreateView.as_view(), name = "cursos-vbc-crear"),
    
    #----Clases para eliminar informacion----
    path("cursos-vbc/eliminar/<int:pk>", views.CursoDeleteView.as_view(), name= "cursos-vbc-eliminar"),
    
    #----Clases para editar informacion----
    path("cursos-vbc/editar/<int:pk>", views.CursoUpdateView.as_view(), name= "cursos-vbc-editar"),
]

