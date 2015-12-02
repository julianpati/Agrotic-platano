from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import userForm
from models import perfil
from models import perfilForm
from models import formularioEditarCuenta
from models import formularioEditarPerfil
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect
from django.template import RequestContext
from models import cultivoForm
from models import cultivo
from models import loteForm
from models import lote
from models import formularioEditarLote
from models import formularioEditarCultivo


# Create your views here.



def principal(request):
    user = request.user.perfil
    if user.tipoUsuario =='D':
        return render(request,"paginaDueno.html",{})
    if user.tipoUsuario =='J':
        return render(request,"paginaJefe.html",{})
    if user.tipoUsuario =='T':
        return render(request,"paginaTrabajador.html",{})


def gestion_usuarios_dueno(request):
    user = request.user.perfil
    if user.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        return render(request,"GUD.html",{})




def dueno_crear_cuenta(request):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        if request.method == 'POST':
            form = userForm(request.POST)

            if form.is_valid():
                new_user = form.save()
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                return HttpResponseRedirect('/dueno_crear_perfil/')
        else:
            form = userForm() # Unbound form

        return render(request,"duenoCrearCuenta.html",{'form' : form})




def dueno_crear_perfil(request):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        if request.method == 'POST':
            form = perfilForm(request.POST)

            if form.is_valid():
                new_user = form.save()
                new_user.tipoUsuario='J'
                new_user.save()
                return HttpResponseRedirect('/gestion_usuarios_dueno/')
        else:
            form = perfilForm() # Unbound form

        return render(request,"duenoCrearPerfil.html",{'form' : form})




def dueno_editar_cuentas(request):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        cuentas= perfil.objects.filter(tipoUsuario='J')
        return render(request,'dueno_editar_cuentas.html', {'cuentas': cuentas})






def dueno_editar_cuenta(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        c= User.objects.get(username=id_user)
        if request.method == 'POST':
            form = formularioEditarCuenta(request.POST, request.FILES)
            if form.is_valid():
                Nombre = form.cleaned_data['first_name']
                Apellidos = form.cleaned_data['last_name']
                Email = form.cleaned_data['email']
                c.first_name = Nombre
                c.last_name = Apellidos
                c.email = Email
                c.save()
                datos = {'cuenta': c}
                return render_to_response('jefeEditado.html', datos, context_instance=RequestContext(request))
                #return HttpResponseRedirect('/dueno_editar_perfil/{{id_user}}/')
        if request.method == 'GET':
            form = formularioEditarCuenta(initial={
                                'Nombre': c.first_name,
                                'Apellidos': c.last_name,
                                'Email': c.email,
            }, instance= c)

        ctx = {
            'form': form,
            'cuenta': c
        }
        return render_to_response('duenoEditarCuenta.html', ctx, context_instance=RequestContext(request))




def dueno_editar_perfil(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        c= perfil.objects.get(user=id_user)
        if request.method == 'POST':
            form = formularioEditarPerfil(request.POST, request.FILES)
            if form.is_valid():
                tipoDocumento = form.cleaned_data['tipoDocumento']
                documento = form.cleaned_data['documento']
                direccion = form.cleaned_data['direccion']
                telefono = form.cleaned_data['telefono']
                fechaDeNacimiento = form.cleaned_data['fechaDeNacimiento']
                c.tipoDocumento = tipoDocumento
                c.documento = documento
                c.direccion = direccion
                c.telefono = telefono
                c.fechaDeNacimiento = fechaDeNacimiento
                c.save()
                return HttpResponseRedirect('/gestion_usuarios_dueno/')
        if request.method == 'GET':
            form = formularioEditarPerfil(initial={
                                'tipoDocumento': c.tipoDocumento,
                                'Documento': c.documento,
                                'Direccion': c.direccion,
                                'Telefono': c.telefono,
                                'fechaDeNacimiento': c.fechaDeNacimiento,
            }, instance= c)

        ctx = {
            'form': form,
            'perfil': c
        }
        return render_to_response('duenoEditarPerfil.html', ctx, context_instance=RequestContext(request))




def dueno_eliminar_cuentas(request):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        cuentas= perfil.objects.filter(tipoUsuario='J')
        return render(request,'duenoEliminarCuentas.html', {'cuentas': cuentas})




def dueno_eliminar_cuenta(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        c= User.objects.get(username=id_user)
        if request.method == 'POST':
            form = formularioEditarCuenta(request.POST, request.FILES)
            if form.is_valid():
                Nombre = form.cleaned_data['first_name']
                Apellidos = form.cleaned_data['last_name']
                Email = form.cleaned_data['email']
                c.first_name = Nombre
                c.last_name = Apellidos
                c.email = Email
                c.delete()
                datos = {'cuenta': c}
                return render_to_response('jefeEliminado.html', datos, context_instance=RequestContext(request))
        if request.method == 'GET':
            form = formularioEditarCuenta(initial={
                                'Nombre': c.first_name,
                                'Apellidos': c.last_name,
                                'Email': c.email,
            }, instance= c)

        ctx = {
            'form': form,
            'cuenta': c
        }
        return render_to_response('duenoEliminarCuenta.html', ctx, context_instance=RequestContext(request))





def gestion_usuarios_jefe(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        return render(request,"GUJ.html",{})




def jefe_crear_cuenta(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        if request.method == 'POST':
            form = userForm(request.POST)

            if form.is_valid():
                new_user = form.save()
                new_user.set_password(form.cleaned_data['password'])
                new_user.save()
                return HttpResponseRedirect('/jefe_crear_perfil/')
        else:
            form = userForm() # Unbound form

        return render(request,"jefeCrearCuenta.html",{'form' : form})




def jefe_crear_perfil(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        if request.method == 'POST':
            form = perfilForm(request.POST)

            if form.is_valid():
                new_user = form.save()
                new_user.tipoUsuario='T'
                new_user.save()
                return HttpResponseRedirect('/gestion_usuarios_jefe/')
        else:
            form = perfilForm() # Unbound form

        return render(request,"jefeCrearPerfil.html",{'form' : form})




def jefe_editar_cuentas(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        cuentas= perfil.objects.filter(tipoUsuario='T')
        return render(request,'jefe_editar_cuentas.html', {'cuentas': cuentas})





def jefe_editar_cuenta(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        c= User.objects.get(username=id_user)
        if request.method == 'POST':
            form = formularioEditarCuenta(request.POST, request.FILES)
            if form.is_valid():
                Nombre = form.cleaned_data['first_name']
                Apellidos = form.cleaned_data['last_name']
                Email = form.cleaned_data['email']
                c.first_name = Nombre
                c.last_name = Apellidos
                c.email = Email
                c.save()
                datos = {'cuenta': c}
                return render_to_response('trabajadorEditado.html', datos, context_instance=RequestContext(request))
                #return HttpResponseRedirect('/dueno_editar_perfil/{{id_user}}/')
        if request.method == 'GET':
            form = formularioEditarCuenta(initial={
                                'Nombre': c.first_name,
                                'Apellidos': c.last_name,
                                'Email': c.email,
            }, instance= c)

        ctx = {
            'form': form,
            'cuenta': c
        }
        return render_to_response('jefeEditarCuenta.html', ctx, context_instance=RequestContext(request))




def jefe_editar_perfil(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        c= perfil.objects.get(user=id_user)
        if request.method == 'POST':
            form = formularioEditarPerfil(request.POST, request.FILES)
            if form.is_valid():
                tipoDocumento = form.cleaned_data['tipoDocumento']
                documento = form.cleaned_data['documento']
                direccion = form.cleaned_data['direccion']
                telefono = form.cleaned_data['telefono']
                fechaDeNacimiento = form.cleaned_data['fechaDeNacimiento']
                c.tipoDocumento = tipoDocumento
                c.documento = documento
                c.direccion = direccion
                c.telefono = telefono
                c.fechaDeNacimiento = fechaDeNacimiento
                c.save()
                return HttpResponseRedirect('/gestion_usuarios_jefe/')
        if request.method == 'GET':
            form = formularioEditarPerfil(initial={
                                'tipoDocumento': c.tipoDocumento,
                                'Documento': c.documento,
                                'Direccion': c.direccion,
                                'Telefono': c.telefono,
                                'fechaDeNacimiento': c.fechaDeNacimiento,
            }, instance= c)

        ctx = {
            'form': form,
            'perfil': c
        }
        return render_to_response('jefeEditarPerfil.html', ctx, context_instance=RequestContext(request))




def jefe_eliminar_cuentas(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        cuentas= perfil.objects.filter(tipoUsuario='T')
        return render(request,'jefeEliminarCuentas.html', {'cuentas': cuentas})




def jefe_eliminar_cuenta(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        c= User.objects.get(username=id_user)
        if request.method == 'POST':
            form = formularioEditarCuenta(request.POST, request.FILES)
            if form.is_valid():
                Nombre = form.cleaned_data['first_name']
                Apellidos = form.cleaned_data['last_name']
                Email = form.cleaned_data['email']
                c.first_name = Nombre
                c.last_name = Apellidos
                c.email = Email
                c.delete()
                datos = {'cuenta': c}
                return render_to_response('trabajadorEliminado.html', datos, context_instance=RequestContext(request))
        if request.method == 'GET':
            form = formularioEditarCuenta(initial={
                                'Nombre': c.first_name,
                                'Apellidos': c.last_name,
                                'Email': c.email,
            }, instance= c)

        ctx = {
            'form': form,
            'cuenta': c
        }
        return render_to_response('jefeEliminarCuenta.html', ctx, context_instance=RequestContext(request))







def gestion_usuarios_trabajador(request):
    u = request.user.perfil
    if u.tipoUsuario != 'T':
        return render(request,"permiso.html",{})
    else:
        return render(request,"GUT.html",{})

def trabajador_editar_cuentas(request):
    return render(request,'trabajador_editar_cuentas.html')





def trabajador_editar_cuenta(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'T':
        return render(request,"permiso.html",{})
    else:
        c= User.objects.get(username=id_user)
        if request.method == 'POST':
            form = formularioEditarCuenta(request.POST, request.FILES)
            if form.is_valid():
                Nombre = form.cleaned_data['first_name']
                Apellidos = form.cleaned_data['last_name']
                Email = form.cleaned_data['email']
                c.first_name = Nombre
                c.last_name = Apellidos
                c.email = Email
                c.save()
                datos = {'cuenta': c}
                return render_to_response('trabajadorEditado.html', datos, context_instance=RequestContext(request))
                #return HttpResponseRedirect('/dueno_editar_perfil/{{id_user}}/')
        if request.method == 'GET':
            form = formularioEditarCuenta(initial={
                                'Nombre': c.first_name,
                                'Apellidos': c.last_name,
                                'Email': c.email,
            }, instance= c)

        ctx = {
            'form': form,
            'cuenta': c
        }
        return render_to_response('trabajadorEditarCuenta.html', ctx, context_instance=RequestContext(request))




def trabajador_editar_perfil(request,id_user):
    u = request.user.perfil
    if u.tipoUsuario != 'T':
        return render(request,"permiso.html",{})
    else:
        c= perfil.objects.get(user=id_user)
        if request.method == 'POST':
            form = formularioEditarPerfil(request.POST, request.FILES)
            if form.is_valid():
                tipoDocumento = form.cleaned_data['tipoDocumento']
                documento = form.cleaned_data['documento']
                direccion = form.cleaned_data['direccion']
                telefono = form.cleaned_data['telefono']
                fechaDeNacimiento = form.cleaned_data['fechaDeNacimiento']
                c.tipoDocumento = tipoDocumento
                c.documento = documento
                c.direccion = direccion
                c.telefono = telefono
                c.fechaDeNacimiento = fechaDeNacimiento
                c.save()
                return HttpResponseRedirect('/gestion_usuarios_trabajador/')
        if request.method == 'GET':
            form = formularioEditarPerfil(initial={
                                'tipoDocumento': c.tipoDocumento,
                                'Documento': c.documento,
                                'Direccion': c.direccion,
                                'Telefono': c.telefono,
                                'fechaDeNacimiento': c.fechaDeNacimiento,
            }, instance= c)

        ctx = {
            'form': form,
            'perfil': c
        }
        return render_to_response('trabajadorEditarPerfil.html', ctx, context_instance=RequestContext(request))



def gestion_de_cultivos_dueno(request):
    u = request.user.perfil
    if u.tipoUsuario != 'D':
        return render(request,"permiso.html",{})
    else:
        return render(request,"gestionDeCultivosDueno.html",{})

def gestion_de_cultivos_jefe(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        return render(request,"gestionDeCultivosJefe.html",{})

def crear_cultivo(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        if request.method == 'POST':
            form = cultivoForm(request.POST)
            if form.is_valid():
                new_cultivo = form.save()
                new_cultivo.jefe = request.user.username
                cantidadLotes = new_cultivo.numeroDeLotes
                encargado = new_cultivo.jefe
                new_cultivo.save()

                return HttpResponseRedirect('/cultivo_creado/')
        else:
            form = cultivoForm() # Unbound form

        return render(request,"crearCultivo.html",{'form' : form})


def cultivo_creado(request):
    return render(request,"cultivoCreado.html",{})

def editar_cultivos(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        cultivos =  cultivo.objects.all()
        return render(request,'editarCultivos.html', {'cultivos': cultivos})

def editar_cultivo(request,id_cultivo):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        c= cultivo.objects.get(idCultivo=id_cultivo)
        if request.method == 'POST':
            form = formularioEditarCultivo(request.POST, request.FILES)
            if form.is_valid():
                numeroDeLotes = form.cleaned_data['numeroDeLotes']
                dimensiones = form.cleaned_data['dimensiones']
                c.numeroDeLotes = numeroDeLotes
                c.dimensiones = dimensiones
                c.save()
                return HttpResponseRedirect('/cultivo_editado/')
        if request.method == 'GET':
            form = formularioEditarCultivo(initial={
                                'NumeroDeLotes': c.numeroDeLotes,
                                'Dimensiones': c.dimensiones,
            }, instance= c)

        ctx = {
            'form': form,
            'cultivo': c

        }
        return render_to_response('editarCultivo.html', ctx, context_instance=RequestContext(request))

def cultivo_editado(request):
    return render(request,"cultivoEditado.html",{})

def gestion_de_lotes(request):
    return render(request,"gestionDeLotes.html",{})

def crear_lote(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        if request.method == 'POST':
            form = loteForm(request.POST)
            if form.is_valid():
                new_lote = form.save()

                new_lote.save()
                return HttpResponseRedirect('/lote_creado/')
        else:
            form = loteForm() # Unbound form

        return render(request,"crearLote.html",{'form' : form})

def lote_creado(request):
    return render(request,"loteCreado.html",{})

def editar_lotes(request):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        lotes= lote.objects.all()
        return render(request,'editarLotes.html', {'lotes': lotes})

def editar_lote(request,id_lote):
    u = request.user.perfil
    if u.tipoUsuario != 'J':
        return render(request,"permiso.html",{})
    else:
        l= lote.objects.get(idLote=id_lote)
        if request.method == 'POST':
            form = formularioEditarLote(request.POST, request.FILES)
            if form.is_valid():
                nombre = form.cleaned_data['nombre']
                dimensiones = form.cleaned_data['dimensiones']
                numeroDeEstacas = form.cleaned_data['numeroDeEstacas']
                idCultivoPertenece = form.cleaned_data['idCultivoPertenece']
                idTrabajadoresAsignados = form.cleaned_data['idTrabajadoresAsignados']
                l.nombre = nombre
                l.dimensiones = dimensiones
                l.numeroDeEstacas = numeroDeEstacas
                l.idCultivoPertenece = idCultivoPertenece
                l.idTrabajadoresAsignados = idTrabajadoresAsignados
                l.save()
                return HttpResponseRedirect('/lote_editado/')
        if request.method == 'GET':
            form = formularioEditarLote(initial={
                                'Nombre': l.nombre,
                                'Dimensiones': l.dimensiones,
                                'NumeroDeEstacas': l.numeroDeEstacas,
                                'IdCultivoPertenece': l.idCultivoPertenece,
                                'IdTrabajadoresAsignados': l.idTrabajadoresAsignados,
            }, instance= l)

        ctx = {
            'form': form,
            'lote': l

        }
        return render_to_response('editarLote.html', ctx, context_instance=RequestContext(request))

def lote_editado(request):
    return render(request,"loteEditado.html",{})

def consultar_lotes(request):
    lotes= lote.objects.all()
    return render(request,'consultarLotes.html', {'lotes': lotes})

def consultar_lote(request, id_lote):
    l= lote.objects.get(idLote=id_lote)
    return  render_to_response('consultarLote.html', {'lote':l }, context_instance=RequestContext(request))