# Create your views here.

from django.shortcuts import render, redirect
from .models import Persona
from .forms import PersonaForm

# para login
#from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm

#se usará en urls.py, retorna la vista index.html
def inicio(request):
    personas = Persona.objects.all() #es un select all del modelo Persona, depende de lo q se retorne ahí traerá acá.
    contexto = {
        'personas':personas
    }
    return render(request,'index.html', contexto)


#función crear persona, usa get para cargar el formulario, y post para enviarlo
def crearPersona(request):
    if request.method == 'GET': #si es por get, mostrar formulario
        form = PersonaForm()
        contexto = {
        'form':form
    }
    else:
        form = PersonaForm(request.POST)
        contexto = {
        'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)


#edita por id,se obtiene la persona, si existe ese id, se llena el form, si no, se envían los datos y se edita.
def editarPersona(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'GET':
        form = PersonaForm(instance = persona)
        contexto = {
            'form':form
        }
    else:
        form = PersonaForm(request.POST, instance = persona)
        contexto = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_persona.html', contexto)


def eliminarPersona(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('index')


# para login
def home(request): 
	return render(request, 'index.html', {})

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Estás dentro lml '))
			return redirect('index') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Te haz desconectado :('))
	return redirect('login')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Estás registrado. Felicidades!'))
			return redirect('index')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'register.html', context)

def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Haz editado tu perfil'))
			return redirect('index')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'edit_profile.html', context)
	#return render(request, 'authenticate/edit_profile.html',{})



def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('Haz editado tu contraseña exitosamente'))
			return redirect('index')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'change_password.html', context)    