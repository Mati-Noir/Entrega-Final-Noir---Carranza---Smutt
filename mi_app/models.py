from hashlib import blake2b
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.camada}"

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellido = models.CharField(max_length=40)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido} {self.Email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.email} {self.profesion}"





class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    avatar = models.ImageField(upload_to = 'avatars', null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.user.username

class Review(models.Model):
    title = models.CharField(max_length = 30)
    content = RichTextField()
    image = models.ImageField(upload_to = 'reviews', null = True, blank = True)
    author = models.ForeignKey(Publisher, on_delete = models.DO_NOTHING)
    is_headline = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True)
    date_published = models.DateTimeField()



class Products(models.Model):
    title = models.CharField(max_length = 30)
    content = RichTextField()
    image = models.ImageField(upload_to = 'reviews', null = True, blank = True)
    author = models.ForeignKey(Publisher, on_delete = models.DO_NOTHING)
    date_updated = models.DateTimeField(auto_now = True)
    date_published = models.DateTimeField()
