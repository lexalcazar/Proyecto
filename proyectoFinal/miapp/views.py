from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'miapp/inicio.html')
# Vista para ver la lista de usuarios
def ver_usuarios(request):
    from .models import Usuario
    usuarios = Usuario.objects.all()
    return render(request, 'miapp/ver_usuarios.html', {'usuarios': usuarios})