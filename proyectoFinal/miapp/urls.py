from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('usuarios/', views.ver_usuarios, name='ver_usuarios'),
]