from typing import Any
from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpRequest
from .models import Author,Post,Categoria
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name','email'] 
    list_filter = ['email',]
    list_per_page = 10
    actions_on_bottom = True
    list_display_links = ['full_name','email']
    
    
    def save_model(self,request,obj,form,change):
        obj.user = request.user
        super().save_model(request,obj,form,change)

    def delete_model(self, request: HttpRequest, obj: Author) -> None:
        return super().delete_model(request, obj)
    

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['title','created_at',]
    date_hierarchy = 'created_at'
    list_per_page = 10
    ordering = ['-created_at']
    list_display_links = ['title','created_at']
    
    def save_model(self, request: HttpRequest, obj: Post, form: ModelForm, change: bool) -> None:
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request: HttpRequest, obj: Post) -> None:
        return super().delete_model(request, obj)
    

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    
    

    def get_readonly_fields(self, request, obj=None):
        readonly = super().get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            readonly.append("name")
        return readonly