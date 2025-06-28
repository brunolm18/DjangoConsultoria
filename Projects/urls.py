from django.urls import path
from . import views
from .views import register, user_login,dashboard,AsesoriaListView,AsesoriaCreateView,AsesoriaUpdateView,AsesoriaDeleteView,AsesoriaDetailView

app_name = 'Projects'

urlpatterns = [
    path('',views.index_view,name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/',dashboard,name='dashboard'),

     path('asesorias/', AsesoriaListView.as_view(), name='asesorias_list'),
     path('asesorias/<int:pk>/', AsesoriaDetailView.as_view(), name='asesoria_detail'),
    path('asesorias/nueva/', AsesoriaCreateView.as_view(), name='asesoria_create'),
    path('asesorias/<int:pk>/editar/', AsesoriaUpdateView.as_view(), name='asesoria_update'),
    path('asesorias/<int:pk>/eliminar/', AsesoriaDeleteView.as_view(), name='asesoria_delete'),

]