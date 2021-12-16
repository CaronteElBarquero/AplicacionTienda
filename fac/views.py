from django.shortcuts import render, redirect
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime

from .models import Cliente, FacturaEnc, FacturaDet, Producto
from bases.views import SinPrivilegios
from .forms import ClienteForm
from bases.views import VistaBaseCreate, VistaBaseEdit

from django.contrib.auth import authenticate

from django.contrib import messages

import inv.views as inv


#################################################### CLIENTES ####################################################

class ClienteView(SinPrivilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required="fac.view_cliente"


class ClienteNew(VistaBaseCreate):
    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.add_cliente"


class ClienteEdit(VistaBaseEdit):

    model = Cliente
    template_name = "fac/cliente_form.html"
    form_class = ClienteForm
    success_url = reverse_lazy("fac:cliente_list")
    permission_required = "fac.change_cliente"



@login_required(login_url="/login/")
@permission_required("fac.change_cliente",login_url="/login/")
def clienteInactivar(request,id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method == "POST":
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse("OK")
        return HttpResponse("FAIL")
    return HttpResponse("FAIL")


##################################################################################################################



#################################################### FACTURAS ####################################################


class FacturaView(SinPrivilegios, generic.ListView):
    model = FacturaEnc
    template_name = "fac/factura_list.html"
    context_object_name = "obj"
    permission_required = "fac.view_facturaenc"



@login_required(login_url='/login/')
@permission_required('fac.change_facturasenc', login_url='bases:sin_privilegios')
def facturas(request, id = None):
    template_name = 'fac/facturas.html'


    detalle = {}
    clientes = Cliente.objects.filter(estado = True)

    if request.method == "GET":
        enc = FacturaEnc.objects.filter(pk=id).first()

        if not enc:
            encabezado = {
                'id':0,
                'fecha':datetime.today(),
                'cliente':0,
                'sub_total':0.00,
                'descuento':0.00,
                'total':0.00,

            }
            detalle = None
        else:
            encabezado = {
                'id':enc.id,
                'fecha':enc.fecha,
                'cliente':enc.cliente,
                'sub_total':enc.sub_total,
                'descuento':enc.descuento,
                'total':enc.total,



            }

            detalle = FacturaDet.objects.filter(factura=enc)

        contexto = {"enc":encabezado, "det":detalle, "clientes":clientes}

    if request.method == "POST":
        cliente = request.POST.get("enc_cliente")
        fecha = request.POST.get("fecha")
        

        cli = Cliente.objects.get(pk=cliente)

        if not id:
            enc = FacturaEnc(
                cliente = cli,
                fecha = fecha
            )

            if enc:
                enc.save()
                id = enc.id
        else:
            enc = FacturaEnc.objects.filter(pk=id).first()
            if enc:
                enc.cliente = cli
                enc.save()
        
        if not id:
            messages.error(request,'No Se Puede Continuar, No Se Detecto No. De Factura')
            return redirect("fac:factura_list")

        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        s_total = request.POST.get("sub_total_detalle")
        descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")
       


        prod = Producto.objects.get(codigo=codigo)
        det = FacturaDet(
            factura = enc,
            producto = prod,
            cantidad = cantidad,
            precio = precio,
            sub_total = s_total,
            descuento = descuento,
            total = total,
        )

        if det:
            det.save()


        return redirect("fac:factura_edit",id=id)


    return render(request, template_name, contexto)

    

class ProduView(inv.ProductoView):
    template_name = "fac/buscar_producto.html"



def borrar_detalle_factura(request, id):

    
    template_name = "fac/factura_borrar_detalle.html"

    det = FacturaDet.objects.get(pk=id)

    if request.method=="GET":
        context={"det":det}

    if request.method == "POST":
        usr = request.POST.get("usuario")
        pas = request.POST.get("pass")

        user =authenticate(username=usr,password=pas)

        if not user:
            return HttpResponse("Usuario o Clave Incorrecta")
        
        if not user.is_active:
            return HttpResponse("Usuario Inactivo")

        if user.is_superuser or user.has_perm("fac.sup_caja_facturadet"):
            det.id = None
            det.cantidad = (-1 * det.cantidad)
            det.sub_total = (-1 * det.sub_total)
            det.descuento = (-1 * det.descuento)
            det.total = (-1 * det.total)
  
            det.save()

            return HttpResponse("ok")

        return HttpResponse("Usuario No Autorizado")
    
    return render(request,template_name,context)


