from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse 
import json


from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto

from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UMForm, ProductoForm
from bases.views import VistaBaseCreate, VistaBaseEdit #Funciones Creadas en bases/bases.view para ahorrar codigo a traves de Herencia

from bases.views import SinPrivilegios





########################################### MODEL CATEGORIA ########################################### 

#Lista  Formulario 
class CategoriaView(SinPrivilegios, generic.ListView):

    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj" #Nombre que resive el query set que se haga en la base de datos, es una variable que se pasa
    

#Crea La Categoria
class CategoriaNew(VistaBaseCreate):
    model = Categoria
    permission_required="inv.add_categoria"
    template_name = "inv/categoria_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list")


#Edita La Categoria
class CategoriaEdit(VistaBaseEdit):
    model = Categoria
    permission_required="inv.change_categoria"
    template_name = "inv/categoria_form.html"
    form_class = CategoriaForm
    success_url = reverse_lazy("inv:categoria_list") #Nos Regresa A La Lista De Categoria Cuando Se Llena Un Formulario



#Borrar los archivos (NO ES NECESARIO YA QUE DESACTIVAMOS Y ACTIVAMOS)
class CategoriaDel(SinPrivilegios, generic.DeleteView):
    model = Categoria
    template_name = "inv/catalogos_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:categoria_list")



@login_required(login_url='/login')
@permission_required('inv.change_categoria',login_url='/login/')
def categoriaInactivar(request, id):
    template_name = 'inv/inactivar_cat.html'
    contexto = {}

    cat = Categoria.objects.filter(pk=id).first() #Consulta al proveedor y nos devolvera el proveedor con la primary key que es igual al id

    if not cat:
        return HttpResponse('Categoria No Existe' + str(id)) # Si el proveedor no existe nos dira el msj y el id del proveedor

    
    #Nos devuelve la consulta que le hicimos en este caso el proveedor
    if request.method == 'GET':
        contexto={'obj':cat}


    if request.method == 'POST':
        cat.estado = False
        cat.save()
        contexto = {'obj':'OK'}
        return HttpResponse('    ➔ Se Ha Inactivado La Categoría ✘')


    return render(request,template_name,contexto)

########################################################################################################### 




########################################### MODEL SUB CATEGORIA ###########################################



#Lista  Formulario 
class SubCategoriaView(SinPrivilegios, generic.ListView):

    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    


#Crea La Sub Categoria
class SubCategoriaNew(VistaBaseCreate):
    model = SubCategoria
    permission_required="inv.add_subcategoria"
    template_name = "inv/subcategoria_form.html"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list") #Nos Regresa A La Lista De Categoria Cuando Se Llena Un Formulario



#Actualiza los registros
class SubCategoriaEdit(VistaBaseEdit):
    model = SubCategoria
    permission_required="inv.change_subcategoria"
    template_name = "inv/subcategoria_form.html"
    form_class = SubCategoriaForm
    success_url = reverse_lazy("inv:subcategoria_list") #Nos Regresa A La Lista De Categoria Cuando Se Llena Un Formulario



#Borrar los archivos (NO SE OCUPA ESTA FUNCION YA QUE SE ACTIVA Y DESACTIVA LA SUBCATEGORIA)
class SubCategoriaDel(SinPrivilegios, generic.DeleteView):
    model = SubCategoria
    template_name = "inv/catalogos_del.html"
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:subcategoria_list")



@login_required(login_url='/login')
@permission_required('inv.change_subcategoria',login_url='/login/')
def subcategoriaInactivar(request, id):
    template_name = 'inv/inactivar_sub.html'
    contexto = {}

    sub = SubCategoria.objects.filter(pk=id).first() #Consulta al proveedor y nos devolvera el proveedor con la primary key que es igual al id

    if not sub:
        return HttpResponse('Sub Categoria No Existe' + str(id)) # Si el proveedor no existe nos dira el msj y el id del proveedor

    
    #Nos devuelve la consulta que le hicimos en este caso el proveedor
    if request.method == 'GET':
        contexto={'obj':sub}


    if request.method == 'POST':
        sub.estado = False
        sub.save()
        contexto = {'obj':'OK'}
        return HttpResponse('➔ Se Ha Inactivado La Sub Categoría ✘')


    return render(request,template_name,contexto)


###########################################################################################################




################################################ MODEL MARCA ##############################################


class MarcaView(SinPrivilegios, generic.ListView):

    permission_required = "inv.view_marca"
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"
    


#Crea La Marca
class MarcaNew(VistaBaseCreate):
    model = Marca
    permission_required="inv.add_marca"
    template_name = "inv/marca_form.html"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")


 
#Edita La Marca
class MarcaEdit(VistaBaseEdit):
    model = Marca
    permission_required="inv.change_marca"
    template_name = "inv/marca_form.html"
    form_class = MarcaForm
    success_url = reverse_lazy("inv:marca_list")



@login_required(login_url='/login')
@permission_required('inv.change_marca',login_url='/login/')
def marcaInactivar(request, id):
    template_name = 'inv/inactivar_mar.html'
    contexto = {}

    marc = Marca.objects.filter(pk=id).first() #Consulta al proveedor y nos devolvera el proveedor con la primary key que es igual al id

    if not marc:
        return HttpResponse('La Marca No Existe' + str(id)) # Si el proveedor no existe nos dira el msj y el id del proveedor

    
    #Nos devuelve la consulta que le hicimos en este caso el proveedor
    if request.method == 'GET':
        contexto={'obj':marc}


    if request.method == 'POST':
        marc.estado = False
        marc.save()
        contexto = {'obj':'OK'}
        return HttpResponse('➔ Se Ha Inactivado La Marca ✘')


    return render(request,template_name,contexto)


###########################################################################################################




########################################### MODEL UNIDAD MEDIDA ###########################################


class UMView(SinPrivilegios, generic.ListView):

    permission_required = "inv.view_unidadmedida"
    model = UnidadMedida
    template_name = "inv/um_list.html"
    context_object_name = "obj"
    

    def form_valid(self, form):
        form.instance.usuarioCrea = self.request.user
        print(self.request.user.id)
        return super().form_valid(form)



#Crea La Unidad De Medida
class UMNew(VistaBaseCreate):
    model = UnidadMedida
    permission_required = "inv.add_unidadmedida"
    template_name="inv/um_form.html"
    form_class = UMForm
    success_url= reverse_lazy("inv:um_list")



class UMEdit(VistaBaseEdit):
    model = UnidadMedida
    permission_required="inv.change_unidadmedida"
    template_name = "inv/um_form.html"
    form_class = UMForm
    success_url = reverse_lazy("inv:um_list")



@login_required(login_url='/login')
@permission_required('inv.change_unidadmedida',login_url='/login/')
def umInactivar(request, id):
    template_name = 'inv/inactivar_um.html'
    contexto = {}

    um = UnidadMedida.objects.filter(pk=id).first() #Consulta al proveedor y nos devolvera el proveedor con la primary key que es igual al id

    if not um:
        return HttpResponse('La Marca No Existe' + str(id)) # Si el proveedor no existe nos dira el msj y el id del proveedor

    
    #Nos devuelve la consulta que le hicimos en este caso el proveedor
    if request.method == 'GET':
        contexto={'obj':um}


    if request.method == 'POST':
        um.estado = False
        um.save()
        contexto = {'obj':'OK'}
        return HttpResponse('➔ Se Ha Inactivado La Unidad De Medida ✘')


    return render(request,template_name,contexto)


########################################################################################################




############################################# MODEL PRODUCTO ############################################


class ProductoView(SinPrivilegios, generic.ListView):

    permission_required = "inv.view_producto"
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"


class ProductoNew(VistaBaseCreate):
    model = Producto
    permission_required="inv.add_producto"
    template_name = "inv/producto_form.html"
    form_class = ProductoForm
    success_url= reverse_lazy("inv:producto_list")



class ProductoEdit(VistaBaseEdit):
    model = Producto
    permission_required="inv.change_producto"
    template_name = "inv/producto_form.html"
    form_class = ProductoForm
    success_url = reverse_lazy("inv:producto_list")



@login_required(login_url='/login/')
@permission_required('inv.change_producto',login_url="/login/")
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto = {}
    template_name = "inv/catalogos_del.html"

    if not prod:
         return redirect("inv:producto_list")

    
    if request.method == 'GET':
        contexto = {'obj': prod}


    if request.method == 'POST':
        prod.estado = False
        prod.save()
        return redirect("inv:producto_list")
    
    return render(request,template_name,contexto)


@login_required(login_url='/login')
@permission_required('inv.change_marca',login_url='/login/')
def productoInactivar(request, id):
    template_name = 'inv/inactivar_prod.html'
    contexto = {}

    produ = Producto.objects.filter(pk=id).first() #Consulta al proveedor y nos devolvera el proveedor con la primary key que es igual al id

    if not produ:
        return HttpResponse('La Marca No Existe' + str(id)) # Si el proveedor no existe nos dira el msj y el id del proveedor

    
    #Nos devuelve la consulta que le hicimos en este caso el proveedor
    if request.method == 'GET':
        contexto={'obj':produ}


    if request.method == 'POST':
        produ.estado = False
        produ.save()
        contexto = {'obj':'OK'}
        return HttpResponse('➔ Se Ha Inactivado El Producto ✘')


    return render(request,template_name,contexto)


######################################################################################################