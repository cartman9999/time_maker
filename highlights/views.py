from django.shortcuts import render, redirect 
from django.contrib import messages
from django.http import HttpResponse
# from django.forms import inlineformset_factory
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 

from .models import *
from .forms import CreateUserForm, HighlightForm, ProfileForm
from .decorators import unauthenticated_user, allowed_users

@unauthenticated_user
def registerPage(request):
    form_register = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada exitosamente')
            return redirect('login')
    
    context = { 'form_register': form_register }
    return render(request, 'auth/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username o Contraseña incorrectos')
        
    context={}
    return render(request, 'auth/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')  
def home(request):
    current_user = request.user
    current_user_id = str(current_user.id)
    
    print("current_user")
    print(current_user)
    print(current_user_id)
    
    highlights = Highlight.objects.filter(user_id=current_user_id)
    delivered = Highlight.objects.filter(user_id=current_user_id, completed=1)
    pending = Highlight.objects.filter(user_id=current_user_id, completed=0)
    
    context = {
                'highlights': highlights,
                'delivered': delivered.count,
                'pending': pending.count
                }

    return render(request, 'highlights/dashboard.html', context)


def userPage(request):
    form = ProfileForm()
    
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            # Obtener el usuario Loggeado
            current_user = request.user
            
            # Agregar más datos al request
            highlight = form.save(commit=False)
            highlight.user_id = current_user.id
            highlight.save()
            return redirect('/')
    
    context = { 'form': form}
    return render(request, 'user.html', context)

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'highlights/products.html', {'products':products})

@login_required(login_url='login')
def highlight(request, pk):
    highlight = Highlight.objects.get(id=pk)
    
    context = {
                'highlight': highlight, 
            }
    return render(request, 'highlights/highlight.html', context)

@login_required(login_url='login')
def createHighlight(request):
    form = HighlightForm()
    
    if request.method == 'POST':
        form = HighlightForm(request.POST)

        if form.is_valid():
    
            # Obtener el usuario Loggeado
            current_user = request.user
            # print("USER")
            # print(current_user)
            # print("ID USER")
            # print(current_user.id)
            # print(type(current_user.id))
            
            # Agregar más datos al request
            highlight = form.save(commit=False)
            highlight.user_id = current_user.id
            highlight.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'highlights/create_highlight.html', context)

@login_required(login_url='login')
def updateHighlight(request, pk):

	highlight = Highlight.objects.get(id=pk)
	form = HighlightForm(instance=highlight)

	if request.method == 'POST':
		form = HighlightForm(request.POST, instance=highlight)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form': form}
	return render(request, 'highlights/create_highlight.html', context)

@login_required(login_url='login')
def deleteHighlight(request, pk):
	highlight = Highlight.objects.get(id=pk)
	if request.method == "POST":
		highlight.delete()
		return redirect('/')

	context = {'item': highlight}
	return render(request, 'highlights/delete.html', context)