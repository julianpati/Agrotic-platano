# -*- encoding: utf-8 -*-

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


# Create your models here.

class perfil(models.Model):
    TIPOS_DE_USUARIO = (
        ('D','Dueño'),
        ('J','Jefe'),
        ('T','Trabajador'),
    )

    TIPOS_DE_DOCUMENTO = (
        ('C.C','Cedula de ciudadania'),
        ('T.I','Tarjeta de identidad'),
    )

    TIPOS_GENERO = (
        ('M','Masculino'),
        ('F','Femenino'),
    )
    user = models.OneToOneField(User)
    tipoUsuario = models.CharField(max_length=10, choices=TIPOS_DE_USUARIO)
    genero=models.CharField(max_length=10, choices=TIPOS_GENERO)
    tipoDocumento = models.CharField(max_length=20, choices= TIPOS_DE_DOCUMENTO)
    documento=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    telefono=models.BigIntegerField()
    fechaDeNacimiento = models.DateField()

class perfilForm(ModelForm):
    class Meta:
        model = perfil
        fields = ('user','genero','tipoDocumento','documento','direccion','telefono','fechaDeNacimiento')



class userForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class formularioEditarCuenta(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class formularioEditarPerfil(ModelForm):
    class Meta:
        model = perfil
        fields = ('tipoDocumento','documento','direccion','telefono','fechaDeNacimiento')


class cultivo(models.Model):
    idCultivo = models.IntegerField(primary_key=True)
    numeroDeLotes = models.IntegerField()
    jefe = models.CharField(max_length=20)
    dimensiones = models.IntegerField("dimensiones en metros cuadrados")
    nombre = models.CharField(max_length=10)


class cultivoForm(ModelForm):
    class Meta:
        model = cultivo
        fields = ('idCultivo','numeroDeLotes', 'dimensiones', 'nombre')


class lote(models.Model):
    idLote = models.IntegerField(primary_key= True)
    nombre = models.CharField(max_length=10)
    dimensiones = models.IntegerField("dimensiones en metros cuadrados")
    numeroDeEstacas = models.IntegerField()
    idCultivoPertenece = models.IntegerField("Cultivo al que pertenece")
    idTrabajadoresAsignados = models.ManyToManyField(User)

class loteForm(ModelForm):
    class Meta:
        model = lote
        fields = '__all__'

class formularioEditarLote(ModelForm):
    class Meta:
        model = lote
        fields = ('nombre','dimensiones','numeroDeEstacas','idCultivoPertenece','idTrabajadoresAsignados')

class variablesDeEstado(models.Model):
    TIPOS_YEMA = (
        ('V','Vegetativa'),
        ('F','Flora'),
    )
    TIPOS_TALLO = (
        ('S','Subterraneo'),
        ('A','Aereo'),
    )
    TIPOS_BELLOTA = (
        ('P','Presente'),
        ('A','Ausente'),
    )
    idLote = models.IntegerField(primary_key = True)
    vainas = models.IntegerField()
    longitudSeudopeciolo = models.IntegerField()
    diametroSeudopeciolo = models.IntegerField()
    longitudNervaduraCentral = models.IntegerField("Longitud de nervadura central")
    diametroNervaduraCentral = models.IntegerField("Diametro de nervadura central")
    yema = models.CharField(max_length= 10, choices = TIPOS_YEMA)
    tallo = models.CharField(max_length= 10, choices = TIPOS_TALLO)
    bellota = models.CharField(max_length= 10, choices= TIPOS_BELLOTA)
    inflorescencia = models.IntegerField("Longitud de inflorescencia")

class formularioVariablesDeEstado(ModelForm):
    class Meta:
        model = variablesDeEstado
        fields = '__all__'

class formularioEditarCultivo(ModelForm):
    class Meta:
        model = cultivo
        fields = ('numeroDeLotes', 'dimensiones')
