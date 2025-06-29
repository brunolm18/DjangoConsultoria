from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=100,verbose_name="Project Name")
    image = models.ImageField(upload_to="projects_images/",verbose_name="Image")
    description = models.CharField(max_length=500,verbose_name="Description",default="Hola")
    technologies = models.CharField(max_length=200,verbose_name="Technologies")
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
    
    
        
class Asesoria(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    creada = models.DateTimeField(auto_now_add=True)
    zoom_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return f"Asesoría de {self.user.username} sobre {self.tema}"
 