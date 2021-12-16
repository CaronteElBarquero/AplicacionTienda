from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin




class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):

    login_url = 'bases:login'
    raise_exception = False
    redirect_field_name = "redirect_to"


    def handle_no_permission(self):
        
        #Importamos usuario anonimo
        from django.contrib.auth.models import AnonymousUser

        #Esta funciom nos sirve por si no estamos logeados no pueda entrar a ninguna otra direccion
        if not self.request.user == AnonymousUser():
            self.login_url = 'bases:sin_privilegios'

        return HttpResponseRedirect(reverse_lazy(self.login_url))
        


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'bases:login'



class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    template_name = "bases/sin_privilegios.html"




#################################################### FUNCIONES PARA MODELS ####################################################

#Esta funcion esta creada con el objetivo de ahorrar codigo (Heredar) al momento de que se quiera crear un nuevo registro 
class VistaBaseCreate(SuccessMessageMixin, SinPrivilegios, generic.CreateView):

    context_object_name = 'obj'
    success_message = " ➔ Registro Creado Con Éxito ✔"

    #Sobreescribimos este metodo para obtener el id del usuario qe esta logeado en ese momento
    def form_valid(self, form):

        form.instance.usuarioCrea = self.request.user#Toma El Usuario Que Esta Logeado Y Lo Guarda En El Formulario
        return super().form_valid(form)




#Esta funcion esta creada con el objetivo de ahorrar codigo (Heredar) al momento de que se quiera editar un nuevo registro
class VistaBaseEdit(SuccessMessageMixin, SinPrivilegios, generic.UpdateView):

    context_object_name = 'obj'
    success_message = " ➔ Registro Actualizado Con Éxito ✔"

     #Sobreescribimos este metodo para obtener el id del usuario qe esta logeado en ese momento
    def form_valid(self, form):
        
        form.instance.usuarioModi = self.request.user.id #Toma El Usuario Modificado Y Lo Guarda En El Formulario
        return super().form_valid(form)


################################################################################################################################