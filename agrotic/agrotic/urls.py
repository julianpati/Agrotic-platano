"""agrotic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from agroticApp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'inicio.html'} , name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^principal/$', 'agrotic.agroticApp.views.principal', name='principal'),


    url(r'^gestion_usuarios_dueno/$', 'agrotic.agroticApp.views.gestion_usuarios_dueno', name='gestion_usuarios_dueno'),
    url(r'^dueno_crear_cuenta/$', 'agrotic.agroticApp.views.dueno_crear_cuenta', name='dueno_crear_cuenta'),
    url(r'^dueno_crear_perfil/$', 'agrotic.agroticApp.views.dueno_crear_perfil', name='dueno_crear_perfil'),
    url(r'^dueno_editar_cuentas/$', 'agrotic.agroticApp.views.dueno_editar_cuentas', name='dueno_editar_cuentas'),
    url(r'^dueno_editar_cuenta/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.dueno_editar_cuenta', name='dueno_editar_cuenta'),
    url(r'^dueno_editar_perfil/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.dueno_editar_perfil', name='dueno_editar_perfil'),
    url(r'^dueno_eliminar_cuentas/$', 'agrotic.agroticApp.views.dueno_eliminar_cuentas', name='dueno_eliminar_cuentas'),
    url(r'^dueno_eliminar_cuenta/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.dueno_eliminar_cuenta', name='dueno_eliminar_cuenta'),


    url(r'^gestion_usuarios_jefe/$', 'agrotic.agroticApp.views.gestion_usuarios_jefe', name='gestion_usuarios_jefe'),
    url(r'^jefe_crear_cuenta/$', 'agrotic.agroticApp.views.jefe_crear_cuenta', name='jefe_crear_cuenta'),
    url(r'^jefe_crear_perfil/$', 'agrotic.agroticApp.views.jefe_crear_perfil', name='jefe_crear_perfil'),
    url(r'^jefe_editar_cuentas/$', 'agrotic.agroticApp.views.jefe_editar_cuentas', name='jefe_editar_cuentas'),
    url(r'^jefe_editar_cuenta/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.jefe_editar_cuenta', name='jefe_editar_cuenta'),
    url(r'^jefe_editar_perfil/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.jefe_editar_perfil', name='jefe_editar_perfil'),
    url(r'^jefe_eliminar_cuentas/$', 'agrotic.agroticApp.views.jefe_eliminar_cuentas', name='jefe_eliminar_cuentas'),
    url(r'^jefe_eliminar_cuenta/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.jefe_eliminar_cuenta', name='jefe_eliminar_cuenta'),
    url(r'^editar_cultivos/$', 'agrotic.agroticApp.views.editar_cultivos', name='editar_cultivos'),
    url(r'^editar_cultivo/(?P<id_cultivo>.*)/$', 'agrotic.agroticApp.views.editar_cultivo', name='editar_cultivo'),
    url(r'^cultivo_editado/$', 'agrotic.agroticApp.views.cultivo_editado', name='cultivo_editado'),




    url(r'^gestion_usuarios_trabajador/$', 'agrotic.agroticApp.views.gestion_usuarios_trabajador', name='gestion_usuarios_trabajador'),
    url(r'^trabajador_editar_cuentas/$', 'agrotic.agroticApp.views.trabajador_editar_cuentas', name='trabajador_editar_cuentas'),
    url(r'^trabajador_editar_cuenta/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.trabajador_editar_cuenta', name='trabajador_editar_cuenta'),
    url(r'^trabajador_editar_perfil/(?P<id_user>.*)/$', 'agrotic.agroticApp.views.trabajador_editar_perfil', name='trabajador_editar_perfil'),

    url(r'^gestion_de_cultivos_dueno/$', 'agrotic.agroticApp.views.gestion_de_cultivos_dueno', name='gestion_de_cultivos_dueno'),
    url(r'^gestion_de_cultivos_jefe/$', 'agrotic.agroticApp.views.gestion_de_cultivos_jefe', name='gestion_de_cultivos_jefe'),
    url(r'^crear_cultivo/$', 'agrotic.agroticApp.views.crear_cultivo', name='crear_cultivo'),
    url(r'^cultivo_creado/$', 'agrotic.agroticApp.views.cultivo_creado', name='cultivo_creado'),
    url(r'^gestion_de_lotes/$', 'agrotic.agroticApp.views.gestion_de_lotes', name='gestion_de_lotes'),
    url(r'^crear_lote/$', 'agrotic.agroticApp.views.crear_lote', name='crear_lote'),
    url(r'^lote_creado/$', 'agrotic.agroticApp.views.lote_creado', name='lote_creado'),
    url(r'^editar_lotes/$', 'agrotic.agroticApp.views.editar_lotes', name='editar_lotes'),
    url(r'^editar_lote/(?P<id_lote>.*)/$', 'agrotic.agroticApp.views.editar_lote', name='editar_lote'),
    url(r'^lote_editado/$', 'agrotic.agroticApp.views.lote_editado', name='lote_editado'),
    url(r'^consultar_lotes/$', 'agrotic.agroticApp.views.consultar_lotes', name='consultar_lotes'),
    url(r'^consultar_lote/(?P<id_lote>.*)/$', 'agrotic.agroticApp.views.consultar_lote', name='consultar_lote'),



]