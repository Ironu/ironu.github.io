from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False, unique=True, verbose_name="nombre")

    def __str__(self):
        return self.nombre


class Artwork(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    titulo = models.CharField(max_length=50)
    img = models.ImageField(null=True, blank=True, upload_to='Artworks/%Y/%m/%d',help_text="Seleccione una imagen para mostrar",)
    video = models.FileField(null=True, blank=True, upload_to='Videos/%Y/%m/%d',help_text="Seleccione un video para mostrar",)
    categoria = models.ForeignKey(Categoria, null=False, blank=True, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

class Comentarios(models.Model):
    noticia = models.ForeignKey('Artwork',related_name='Comentarios', on_delete=models.CASCADE)
    autor =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cuerpo_comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False)

    def aprobarComentario(self):
        self.aprobado = True
        self.save()

