from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length= 100, null=True, blank= True)
    estado = models.BooleanField('Categoria activa/categoria no activa', default= True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombres = models.CharField('Nombres de autor', max_length= 255, null=True, blank=True)
    apellidos = models.CharField('Apellidos de autor', max_length= 255, null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    twitter = models.URLField('Twitter', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    web = models.URLField('Web', null=True, blank=True)
    correo = models.EmailField('Correo electronico', null=True, blank=True)
    estado = models.BooleanField('Autor activo/ no activo', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now= False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)

class Post(models.Model):
    titulo = models.CharField('Título', max_length=90, blank=True, null=True)
    slug = models.CharField('Slug', max_length=100, blank=True, null=True)
    descripcion = models.CharField('Descripción', max_length=110, blank=True, null=True)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255, blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/no publicado', default= True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo