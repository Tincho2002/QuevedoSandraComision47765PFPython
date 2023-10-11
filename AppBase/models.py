from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENERO_OPCIONES = [('accion', 'Acción'), ('aventura', 'Aventura'), ('cficcion', 'CFiccion'), ('comedia', 'Comedia'), ('comerciales', 'Comerciales'), 
                   ('deportes', 'Deportes'), ('documentales', 'Documentales'), ('drama', 'Drama'),('entrevistas', 'Entrevistas'), ('musica', 'Música'), 
                   ('suspenso', 'Suspenso'), ('terror', 'Terror'), ]

GENERO_OPCIONES = sorted(GENERO_OPCIONES, key=lambda x: x[1])

VALORACIONES_OPCIONES = [(i, str(i)) for i in range(1, 11)]

class Pelicula(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_salida = models.DateField()
    genero = models.CharField(max_length=255, choices=GENERO_OPCIONES)
    empresa = models.CharField(max_length=255)
    descripcion = models.TextField()
    valoracion = models.IntegerField(choices=VALORACIONES_OPCIONES, null=False)
    def __str__(self):
        return f"{self.nombre} - {self.genero} - {self.empresa}"

class Resena(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.autor} - {self.pelicula.nombre}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    def __str__(self):
        return f"{self.user} / {self.imagen}"
    
class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.creador} - {self.titulo}"

class Comentario(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='comentarios')
    def __str__(self):
        return f"{self.creador} - {self.tema}"