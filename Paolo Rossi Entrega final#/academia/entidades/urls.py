from django.contrib import admin
from django.urls import path
from .views import home, comprar, comprarForm, comprarUpdate, comprarDelete, profesores, profesoresForm, profesoresUpdate, profesoresDelete, VisitantesList, VisitantesCreate, VisitantesUpdate, loginRequest, register, editProfile, CambiarClave, agregarAvatar
from django.contrib.auth.views import LoginView, LogoutView
from .views import register

urlpatterns = [
    path('', home, name="home"),
    #Compras
    path('comprar/', comprar, name="comprar"),
    path('comprarForm/', comprarForm, name="comprarForm"),
    path('comprarUpdate/<id_comprar>/', comprarUpdate, name="comprarUpdate"),
    path('comprarDelete/<id_comprar>/', comprarDelete, name="comprarDelete"),


    #Productos
    path('profesores/', profesores, name="profesores"),
    path('profesoresForm/', profesoresForm, name="profesoresForm"),
    path('profesoresUpdate/<id_profesores>/', profesoresUpdate, name="profesoresUpdate"),
    path('profesoresDelete/<id_profesores>/', profesoresDelete, name="profesoresDelete"),

    #Visitantes
    path('projects/', VisitantesList.as_view(), name="visitantes"),
    path('visitantesCreate/', VisitantesCreate.as_view(), name="visitantesCreate"),
    path('visitantesUpdate/<int:pk>/', VisitantesUpdate.as_view(), name="visitantesUpdate"),


    #login/logout/registration
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),

    #Edicion
    path('perfil/', editProfile, name="perfil"),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),  
]

