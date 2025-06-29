
from django.db import models

# Create your models here.
class Author(models.Model):
    full_name = models.CharField(max_length=200,verbose_name="Full Name",null=False)
    email = models.EmailField(max_length=200,verbose_name="Email",unique=True,null=False)
    biography = models.TextField(verbose_name="Biography",blank=True)
    country = models.CharField(max_length=20,verbose_name="Country")

    class Meta:
        db_table = "Authors"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        get_latest_by = "email"

    def __str__(self):
        return self.email
    
   
    

class Post(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(upload_to="posts_images",verbose_name="Image")
    text = models.TextField(verbose_name="Text")
    created_at = models.DateTimeField(auto_now_add=True)
        

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "Posts"
        get_latest_by = "created_at"

    
    def __str__(self):
        return f"{self.title} by {self.author.full_name}"
    
class Categoria(models.Model):
    name = models.CharField(max_length=30,verbose_name="Categoria",null=False)
    posts = models.ManyToManyField(Post)

   
    
    class Meta:
        db_table = "Categorias"
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name