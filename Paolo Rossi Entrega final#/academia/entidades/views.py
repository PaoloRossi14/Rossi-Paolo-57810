from django.shortcuts import render, redirect

from .models import *

from .forms import *

from django.urls import reverse_lazy


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required





# Create your views here.
def home(request):
    return render(request,"entidades/index.html")

@login_required
def comprar(request):
    contexto= {"comprar":Compras.objects.all()}
    return render(request,"entidades/comprar.html", contexto)

@login_required
def visitantes(request):
    contexto= {"visitantes":Visitantes.objects.all()}
    return render(request,"entidades/visitantes.html", contexto)

@login_required
def profesores(request):
    contexto= {"profesores":Profesores.objects.all()}
    return render(request,"entidades/profesores.html", contexto)

 # Compras 
@login_required
def comprarForm(request):
    if request.method =="POST":
        miForm = ComprasForm(request.POST)
        if miForm.is_valid():
            comprar_nombre =miForm.cleaned_data.get("nombre")
            comprar_stock=miForm.cleaned_data.get("stock")
            comprar_size=miForm.cleaned_data.get("size")
            comprar_precio=miForm.cleaned_data.get("precio")
            comprar = Compras(nombre=comprar_nombre, stock= comprar_stock, size=comprar_size, precio=comprar_precio)
            comprar.save()
            contexto = {"comprar": Compras.objects.all()}
            return render(request,"entidades/comprar.html", contexto)
    else:
        miForm = ComprasForm()
    return render(request, "entidad/comprarForm.html", {"Form": miForm})
@login_required
def comprarUpdate(request, id_comprar):
    comprar = Compras.objects.get(id=id_comprar)
    if request.method == "POST":
        miForm = ComprasForm(request.POST)
        if miForm.is_valid():
            comprar.nombre =miForm.cleaned_data.get("nombre")
            comprar.stock=miForm.cleaned_data.get("stock")
            comprar.size=miForm.cleaned_data.get("size")
            comprar.precio=miForm.cleaned_data.get("precio")
            comprar.save()
            contexto = {"comprar": Compras.objects.all()}
            return render(request,"entidades/comprar.html", contexto)
    else:
        miForm = ComprasForm(initial={"nombre" : comprar.nombre, "stock" : comprar.stock, "size" : comprar.size, "precio" : comprar.precio})
    return render(request, "entidad/comprarForm.html", {"Form": miForm})
@login_required
def comprarDelete(request, id_comprar):
    comprar = Compras.objects.get(id=id_comprar)
    comprar.delete()
    contexto = {"comprar": Compras.objects.all()}
    return render(request,"entidades/comprar.html", contexto)


            #profesores = Profesores(nombre=profesores_nombre, precio= profesores_edad, stock= profesores_horarios, stock= profesores_profesion)
#Productos
@login_required
def profesoresForm(request):
    if request.method =="POST":
        miForm = ProfesoresForm(request.POST)

        if miForm.is_valid():
            profesores_nombre =miForm.cleaned_data.get("nombre")
            profesores_edad=miForm.cleaned_data.get("edad")
            profesores_horarios=miForm.cleaned_data.get("horarios")
            profesores_profesion=miForm.cleaned_data.get("profesion")
            profesores = Profesores(nombre=profesores_nombre, edad=profesores_edad, horarios=profesores_horarios, profesion=profesores_profesion)
            profesores.save()
            contexto = {"profesores": Profesores.objects.all()}
            return render(request,"entidades/profesores.html", contexto)
    else:
        miForm = ProfesoresForm()
    return render(request, "entidad/profesoresForm.html", {"Form": miForm})

@login_required
def profesoresUpdate(request, id_profesores):
    profesores = Profesores.objects.get(id=id_profesores)
    if request.method == "POST":
        miForm = ProfesoresForm(request.POST)
        if miForm.is_valid():
            profesores_nombre =miForm.cleaned_data.get("nombre")
            profesores_edad=miForm.cleaned_data.get("edad")
            profesores_horarios=miForm.cleaned_data.get("horarios")
            profesores_profesion=miForm.cleaned_data.get("profecion")
            profesores= Profesores(nombre=profesores_nombre, edad=profesores_edad, horarios=profesores_horarios, profesion=profesores_profesion)
            profesores.save()
            contexto = {"profesores": Profesores.objects.all()}
            return render(request,"entidades/profesores.html", contexto)
    else:
        miForm = ProfesoresForm(initial={"nombre" : profesores.nombre, "edad" : profesores.edad, "horarios" : profesores.horarios, "profesion" : profesores.profesion})
    return render(request, "entidad/profesoresForm.html", {"Form": miForm})

@login_required
def profesoresDelete(request, id_profesores):
    profesores = Profesores.objects.get(id=id_profesores)
    profesores.delete()
    contexto = {"profesores": Profesores.objects.all()}
    return render(request,"entidades/profesores.html", contexto)


class VisitantesList(LoginRequiredMixin, ListView):
    model = Visitantes


class VisitantesCreate(LoginRequiredMixin, CreateView):
    model = Visitantes
    fields =["nombre", "apellido", "email"]
    success_url = reverse_lazy("visitantes")


class VisitantesUpdate(LoginRequiredMixin, UpdateView):
    model = Visitantes
    fields =["nombre", "apellido", "email"]
    success_url = reverse_lazy("visitantes")

class VisitantesDelete(LoginRequiredMixin, DeleteView):
    model = Visitantes
    success_url = reverse_lazy("visitantes")




#login/logout/registration

def loginRequest(request):
    if request.method == "POST":
        usuario= request.POST["username"]
        clave= request.POST["password"]
        user= authenticate(request,username=usuario, password=clave)
        if user is not None:
            login(request,user)

            try:
                avatar= object.get(user=request.user.id).imagen.url #error
            except: 
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    miForm= RegistroForm(request.POST)
    if miForm.is_valid():
        User= miForm.cleaned_data.get("username")
        miForm.save()
        return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm})

# Edicion

@login_required
def editProfile(request):
    usuario = request.user
    if request.merhod == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "entidades/editPerfil.html", {"from", miForm})



class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")


def agregarAvatar(request):
    if request.merhod == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen= miForm.cleaned_data["imagen"]
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0 :
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            avatar= Avatar(user=usuario, imagen=imagen)
            avatar.save()
            imagen= Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm(instance=avatar)
    return render(request, "entidades/agregarAvatar.html", {"from", miForm})    
