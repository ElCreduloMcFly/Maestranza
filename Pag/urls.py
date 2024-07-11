from django.contrib import admin
from django.urls import path
from .views import mostrarhome,mostrarcarrito,mostrarherramientas,mostrarinicio,mostrarvendedor,iniciarsesion,registrar,finsesion,mostraragregar,agregarproducto,eliminarproducto,modificarproducto,mostrarproducto,mostrarnuevotrabajador,mostrarmenulogin,mostrarproveedor,mostrarproveedores,agregarequipo,agregarProveedor,mostrarequipos,eliminarproveedor,agregartrabajador,agregarequipos

urlpatterns = [
    path('',mostrarhome,name="MenuPrincipal"),
    path('Carrito/',mostrarcarrito,name="Carrito"),
    path('Herramientas/',mostrarherramientas,name="Herramientas"),
    path('Inicio/',mostrarinicio,name="Sesion"),
    path('Vendedor/',mostrarvendedor,name="Vendedor"),
    path('Proveedor/',mostrarproveedores,name="Proveedor"),
    path('agregarProv/',mostrarproveedor,name="agregarProv"),
    path('agregarEquipo/',agregarequipo,name="agregarEquipo"),
    path('MenuPrincipalLogin/',mostrarmenulogin,name="MenuPrincipalLogin"),
    path('mostrarproducto/',mostraragregar,name="mostrarcategoria"),
    path('mostrarequipos/',mostrarequipos,name="mostrarequipos"),
    path('mostrarnuevotrabajador/',mostrarnuevotrabajador,name="mostrarnuevotrabajador"),
    path('iniciarsesion/', iniciarsesion, name='iniciarsesion'),   
    path('registrar/',registrar,name="registrar"),
    path('finsesion/',finsesion, name='finsesion'),
    path('agregarproducto/',agregarproducto, name='agregarproducto'),
    path('agregartrabajador/',agregartrabajador, name='agregartrabajador'),
    path('agregarEquipos/',agregarequipos, name='agregarEquipos'),
    path('agregarprove/',agregarProveedor, name='agregarprove'),
    path('eliminarproducto/<id_prod>',eliminarproducto, name='eliminarproducto'),
    path('eliminarproveedor/<id_prov>',eliminarproveedor, name='eliminarproveedor'),
    path('mostrarproducto/<int:id_prod>',mostrarproducto, name='mostrarproducto'),
    path('modificarproducto/<int:id_prod>',modificarproducto, name='modificarproducto'),

]