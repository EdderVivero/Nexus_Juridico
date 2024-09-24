from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige al dashboard después de iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'vista/Form_Login.html')

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()
    return render(request, 'vista/form_Registro.html', {'form': form})

@login_required
def dashboard_view(request):
    user_role = request.user.role 
    return render(request, 'vista/dashboard.html', {'user_role': user_role})