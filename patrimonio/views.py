from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Categoria, LugarPatrimonial

def home(request):
    return render(request, 'patrimonio/home.html')

def catalogo(request):
    categoria_id = request.GET.get('categoria')
    categorias = Categoria.objects.all()
    
    if categoria_id:
        lugares = LugarPatrimonial.objects.filter(categoria_id=categoria_id)
    else:
        lugares = LugarPatrimonial.objects.all()
        
    return render(request, 'patrimonio/catalogo.html', {
        'lugares': lugares,
        'categorias': categorias,
    })

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('gestion')
    else:
        form = AuthenticationForm()
    return render(request, 'patrimonio/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def gestion(request):
    lugares = LugarPatrimonial.objects.all()
    return render(request, 'patrimonio/gestion.html', {'lugares': lugares})
