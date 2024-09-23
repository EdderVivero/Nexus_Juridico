from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

# Create your views here.
def saludo (request):
    return HttpResponse("Alo")

def mostrar_formulario (request):
    return render(request, 'vista/Form_Login.html')

