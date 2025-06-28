from django.shortcuts import render,redirect
from .models import Project,Asesoria
from django.contrib.auth import  login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from .forms import AsesoriaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
import os

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse




def index_view(request):
    projects = Project.objects.all()

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        if nombre and correo and asunto and mensaje:
            cuerpo = f"De: {nombre} <{correo}>\n\nMensaje:\n{mensaje}"
            try:
                send_mail(
                    asunto,
                    cuerpo,
                    os.getenv('EMAIL_HOST_USER'),      # Remitente
                    ['brunolezamamendez18@gmail.com'], # Destinatario(s)
                    fail_silently=False,
                )
                messages.success(request, "¡Mensaje enviado con éxito!")
                return redirect('index')
            except Exception as e:
                messages.error(request, f"Error enviando el mensaje: {e}")
        else:
            messages.error(request, "Por favor completa todos los campos.")

    return render(request, 'Projects/index.html', {'projects': projects})


class ProjectDetail(DetailView):
    template_name = 'Projects/project_detail.html'
    context_object_name = 'projects'
    queryset = Project.objects.all()




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                messages.success(request, "Usuario registrado exitosamente. Inicia sesión.")
                return redirect('Projects:login')
            except Exception as e:
                messages.error(request, f"Ocurrió un error al registrar el usuario: {e}")
        else:
            messages.error(request, "Por favor corrige los errores en el formulario.")
    else:
        form = UserRegisterForm()
    return render(request, 'Projects/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Projects:dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'Projects/login.html', {'form': form})  



@login_required
def dashboard(request):
    asesorias = Asesoria.objects.filter(user=request.user)
    return render(request, 'Projects/dashboard.html', {'asesorias': asesorias})



class AsesoriaListView(LoginRequiredMixin, ListView):
    model = Asesoria
    template_name = 'Projects/asesorias_list.html'
    context_object_name = 'asesorias'

    def get_queryset(self):
        return Asesoria.objects.filter(user=self.request.user)
    

class AsesoriaDetailView(LoginRequiredMixin, DetailView):
    model = Asesoria
    template_name = 'Projects/asesoria_detail.html'

    def get_queryset(self):
       
        return Asesoria.objects.filter(user=self.request.user)


class AsesoriaCreateView(LoginRequiredMixin, CreateView):
    model = Asesoria
    form_class = AsesoriaForm
    template_name = 'Projects/asesoria_form.html'
    success_url = reverse_lazy('projects:asesorias_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AsesoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Asesoria
    form_class = AsesoriaForm
    template_name = 'Projects/asesoria_form.html'
    success_url = reverse_lazy('Projects:asesorias_list')

    def get_queryset(self):
        return Asesoria.objects.filter(user=self.request.user)


class AsesoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Asesoria
    template_name = 'Projects/asesoria_confirm_delete.html'
    success_url = reverse_lazy('Projects:asesorias_list')

    def get_queryset(self):
        return Asesoria.objects.filter(user=self.request.user)
    
