from django.urls import path, include

from .views import ClienteView, ClienteNew, ClienteEdit, clienteInactivar, \
                   FacturaView, facturas, ProduView, borrar_detalle_factura

from .reportes import imprimir_factura_recibo

urlpatterns = [

    ########################################### CLIENTES ###########################################

    path('clientes/', ClienteView.as_view(), name="cliente_list"),

    path('clientes/new', ClienteNew.as_view(), name="cliente_new"),

    path('clientes/<int:pk>', ClienteEdit.as_view(), name="cliente_edit"),

    path('clientes/estado/<int:id>', clienteInactivar, name="cliente_inactivar"),

    ########################################### FACTURAS ###########################################

    path('facturas/', FacturaView.as_view(), name="factura_list"),

    path('facturas/new', facturas, name="factura_new"),

    path('facturas/edit/<int:id>',facturas,name="factura_edit"),

    path('facturas/buscar-producto', ProduView.as_view(), name="factura_producto"),

    path('facturas/borrar-detalle/<int:id>',borrar_detalle_factura, name="factura_borrar_detalle"),


    ########################################### IMPRIMIR ###########################################

    path('facturas/imprimir/<int:id>',imprimir_factura_recibo, name="factura_imprimir_one"),
]