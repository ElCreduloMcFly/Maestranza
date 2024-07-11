from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import pregunta,usuario,rol,categoria,producto,proveedor,equipo
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.
def mostrarhome(request):
    productos = producto.objects.all()
    return render(request,'MenuPrincipal.html',{'productos':productos})

def mostrarherramientas(request):
    productos = producto.objects.all()
    return render(request,'herramientas.html',{'productos':productos})

def mostrarinicio(request):
    preguntas = pregunta.objects.all()
    # Pasar los datos al template
    return render(request, 'InicioSeccion_Registro.html', {'preguntas': preguntas})

def mostrarolvido(request):
    return render(request,'olvidocontraseña.html')

def mostrarcarrito(request):
    return render(request,'carrito.html')

def mostrarvendedor(request):
    productos = producto.objects.all()
    return render(request,'inventarioAct.html',{'productos':productos})

def mostrarproveedores(request):
    proveedors = proveedor.objects.all()
    return render(request,'proveedores.html',{'provedores':proveedors})

def mostrarproveedor(request):
    categorias = categoria.objects.all()
    return render(request,'addProveedor.html',{'categorias':categorias})

def mostraragregar(request):
    categorias = categoria.objects.all()
    return render(request,'addproducto.html',{'categorias':categorias})

def mostrarnuevotrabajador(request):
    preguntas = pregunta.objects.all()
    roles = rol.objects.all()
    return render(request,'agregar_trabajador.html',{'preguntas':preguntas,'roles':roles})

def agregarequipo(request):
    # Filtra los roles permitidos para líderes
    roles_lider = rol.objects.filter(nombre_rol__in=["Gerente de Proyectos", "Jefe de Producción"])
    usuarios_lideres = usuario.objects.filter(rol_usu__in=roles_lider)
    
    # Filtra los roles permitidos para integrantes
    rol_integrante = rol.objects.get(nombre_rol="Trabajador de Planta")
    usuarios_integrantes = usuario.objects.filter(rol_usu=rol_integrante)
    
    return render(request, 'agregarequipo.html',{'usuarios_lideres': usuarios_lideres,'usuarios_integrantes': usuarios_integrantes})

def mostrarequipos(request):
    equipos = equipo.objects.all()
    return render(request,'Equipos.html',{'equipos':equipos})

def mostrarmenulogin(request):
    productos = producto.objects.all()
    return render(request,'MenuPrincipallogin.html',{'productos':productos})

def mostrarproducto(request,id_prod):
    productos = producto.objects.get(id_prod=id_prod)
    categorias = categoria.objects.all()
    return render(request,'modificarproducto.html',{'productos':productos,'categorias':categorias})

#FUNCIONES DEL USUARIO

def registrar(request):
    rutU = request.POST['rut']
    nombreU = request.POST['name']
    direccionU = request.POST['direccion']
    correoU = request.POST['correo']
    contrasenaU = request.POST['password']
    telefonoU = request.POST['telefono']
    preguntaU = request.POST['pregunta']
    respuestaU = request.POST['rs']
    
    if User.objects.filter(email=correoU).exists():
        return render(request, 'correo_registrado.html')

    user = User.objects.create_user(username = correoU,
                                    email= correoU,
                                    password= contrasenaU)
    
    if "@maestranza.com" in correoU:
        user.is_staff = True    
        roluser = rol.objects.get(nombre_rol = "Administrador")
    else:
        user.is_staff = False
        roluser = rol.objects.get(nombre_rol = "Trabajador de Planta")
    registroPreg = pregunta.objects.get(id_preg = preguntaU)
    
    usuario.objects.create(rut_usu = rutU,nombre_usu = nombreU,correo_usu = correoU,
                           contrasena_usu = contrasenaU,direccion_usu = direccionU,telefono_usu = telefonoU ,
                           rol_usu = roluser, id_preg = registroPreg)
    
    user.is_active = True
    user.save()
    return redirect('Sesion')

def iniciarsesion(request):
    usuario1 = request.POST['correo']
    contra1 = request.POST['clave']

    try: 
        user1 = User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return render(request,'InicioSeccion_Registro.html')

    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        messages.error(request, 'El usuario o la contraseña son incorrectas')
        return render(request,'InicioSeccion_Registro.html')

    usuario2 = usuario.objects.get(correo_usu = usuario1, contrasena_usu= contra1)
    user = authenticate(username = usuario1, password=contra1)

    if user is not None:
        login(request, user)
        if(usuario2.rol_usu.nombre_rol == "Administrador" ):
            return redirect('Vendedor')

        else: 
            return redirect('MenuPrincipalLogin')

    else:
        print("8")

def finsesion(request):
    logout(request)
    return redirect('MenuPrincipal')  

# FIN ACCIONES USUARIO

#ACCIONES ADMINISTRADOR(AGREGAR/MODIFICAR/ELIMINAR PRODUCTOS)

def agregarproducto(request):
    imagenP = request.FILES['imagen']
    nombreP = request.POST['nombre']
    descP = request.POST['descripcion']
    precioP = request.POST['precio']
    stockP = request.POST['stock']
    categoriaP = request.POST['categoria']
    cateescogida = categoria.objects.get(id_categoria=categoriaP)

    producto.objects.create(imagen=imagenP,nombre_prod=nombreP,descripcion=descP,precio=precioP,stock=stockP,id_categoria=cateescogida)
    return render(request,'inventarioAct.html')


def eliminarproducto(request, id_prod):
        eliminar = producto.objects.get(id_prod = id_prod)
        eliminar.delete()
        return redirect('Vendedor')

def modificarproducto(request,id_prod):

    imagenP = request.FILES['imagen']
    nombreP = request.POST['nombre']
    descP = request.POST['descripcion']
    precioP = request.POST['precio']
    stockP = request.POST['stock']
    categoriaP = request.POST['categoria']
    cateescogida = categoria.objects.get(id_categoria=categoriaP)

    prod = producto.objects.get(id_prod=id_prod)

    prod.imagen = imagenP
    prod.nombre_prod = nombreP
    prod.descripcion = descP
    prod.precio = precioP
    prod.stock = stockP
    prod.id_categoria = cateescogida

    prod.save()

    return redirect('Vendedor')


def agregarProveedor(request):
    nombreProv = request.POST['nombre']
    direProv = request.POST['direccion']
    correoProv = request.POST['correo']
    CelProv = request.POST['cel']

    proveedor.objects.create(nombre_prov=nombreProv,direccion_prov=direProv,correo=correoProv,telefono=CelProv)

    return redirect('Proveedor')

def eliminarproveedor(request, id_prov):
        eliminar = proveedor.objects.get(id_prov = id_prov)
        eliminar.delete()
        return redirect('Proveedor')

def agregartrabajador(request):
    rutT = request.POST['rut']
    nombreT = request.POST['nombre']
    correoT = request.POST['correo']
    contrasenaT = request.POST['contrasena']
    direccionT = request.POST['direccion']
    telefonoT = request.POST['telefono']
    pregT = request.POST['pregunta_seguridad']
    rolT = request.POST['rol']

    if User.objects.filter(email=correoT).exists():
        return render(request, 'correo_registrado.html')
    
    
    user = User.objects.create_user(username = correoT,
                                    email= correoT,
                                    password= contrasenaT)
    if rolT == 'Administrador':
            user.is_staff = True  
    else:
            user.is_staff = False

    
    registroPreg = pregunta.objects.get(id_preg = pregT)
    registroRol = rol.objects.get(id_rol=rolT)
    
    usuario.objects.create(rut_usu = rutT,nombre_usu = nombreT,correo_usu = correoT,
                           contrasena_usu = contrasenaT,direccion_usu = direccionT,telefono_usu = telefonoT ,
                           rol_usu = registroRol, id_preg = registroPreg)
        
    # Guardar el usuario para aplicar el cambio de is_staff
    user.is_active = True
    user.save()
    return redirect('Vendedor')


def agregarequipos(request):
    nombreE = request.POST['nombre_equipo']
    nombreP = request.POST['nombre_proyecto']
    lider = request.POST['lider']
    inte1 = request.POST['integrante1']
    inte2 = request.POST['integrante2']
    inte3 = request.POST['integrante3']

    Registrolider = usuario.objects.get(id_usuario=lider)
    Registrointe1 = usuario.objects.get(id_usuario=inte1)
    Registrointe2 = usuario.objects.get(id_usuario=inte2)
    Registrointe3 = usuario.objects.get(id_usuario=inte3)

    equipo.objects.create(nombre_equipo=nombreE, nombre_proyecto=nombreP, lider_proyecto=Registrolider, integrante_1=Registrointe1, integrante_2=Registrointe2, integrante_3=Registrointe3)
    
    return redirect('mostrarequipos')

def eliminarequipo(request, id_equipo):
        eliminar = equipo.objects.get(id_equipo = id_equipo)
        eliminar.delete()
        return redirect('mostrarequipos')