from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('ag-pelicula', agregar_pelicula, name="AgregarPelicula"),
    path('l-peliculas', lista_peliculas, name="ListaPeliculas"),
    path('el-peliculas/<int:id>', eliminar_pelicula, name="EliminarPelicula"),
    path('ed-peliculas/<int:id>', editar_pelicula, name="EditarPelicula"),
    path('ag-resena', agregar_resena, name='AgregarResena'),
    path('l-resenas', lista_resenas, name='ListaResenas'),
    path('el-resenas/<int:id>', eliminar_resena, name="EliminarResena"),
    path('ed-resenas/<int:id>', editar_resena, name="EditarResena"),
    path('busq-pelicula', busqueda_peliculas, name="BusquedaPeliculas"),
    path('buscar-nombre', buscar_nombre, name="BuscarNombre"),
    path('buscar-genero', buscar_genero, name="BuscarGenero"),
    path('buscar-empresa', buscar_empresa, name="BuscarEmpresa"),
    path('buscar-valoracion', buscar_valoracion, name="BuscarValoracion"),
    path('about-me', AboutMe, name="AboutMe"),
    path('foro', lista_temas, name='Foro'),
    path('crear-tema', crear_tema, name='CrearTema'),
    path('ed-tema/<int:pk>', editar_tema, name='EditarTema'),
    path('el-tema/<int:pk>', eliminar_tema, name='EliminarTema'),
    path('foro/<int:pk>/', detalle_tema, name='DetalleTema'),
    path('<int:pk>/crear-coment', crear_comentario, name='CrearComentario'),
]