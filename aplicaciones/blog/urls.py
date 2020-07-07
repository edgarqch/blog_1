from django.urls import path

from .views import home, generales, programacion, videojuegos, tecnologia, tutoriales

urlpatterns = [
    path('',home,name='index'),
    path('generales/',generales,name='generales'),
    path('programacion/',programacion,name='programacion'),
    path('videojuegos/',videojuegos,name='videojuegos'),
    path('tecnologia/',tecnologia,name='tecnologia'),
    path('tutoriales/',tutoriales,name='tutoriales'),
]