from django.db import models

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