from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.usuario.forms import UsuarioForm
from apps.usuario.models import Usuario

def index(request):
	return render(request, 'usuario/index.html')

def usuario_view(request):
	if request.method == 'POST':
		form = UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('usuario:usuario_listar')
	else:
		form = UsuarioForm()
	return render(resquest, 'usuario/usuario_form.html', {'form':form})

def usuario_list(request):
	usuario = Usuario.objects.all().oredr_by('id')
	contexto = {'usuarios':usuario}
	return render(request, 'usuario/usuario_list.html', contexto)


def usuario_edit(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'GET':
		form = UsuarioForm(instance=usuario)
	else:
		form = UsuarioForm(request.POST, instance=usuario)
		if form.is_valid():
			form.save()
		return redirect('usuario:usuario_lista')
	return render(request, 'usuario/usuario_form.html', {'form':form})


def usuario_delete(request, id_usuario):
	usuario = Usuario.objects.get(id=id_usuario)
	if request.method == 'POTS':
		usuario.delete()
		return redirect('usuario:usuario_editar')
	return render(request, 'usuario/usuario_delete.html', {'usuario':usuario})

class UsuarioList(ListView):
	model = Usuario
	template_name = 'usuario/usuario_list.html'

class UsuarioCreate(CreateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/usuario_form.html'
	sucess_url = reverse_lazy('usuario/usuario_listar')

class UsuarioUpdate(UpdateView):
	model = Usuario
	form_class = UsuarioForm
	template_name = 'usuario/usuario_form.html'
	sucess_url = reverse_lazy('usuario:usuario_listar')

class UsuarioDelete(DeleteView):
	model = Usuario
	template_name = 'usuario/usuario_delete.html'
	sucess_url = reverse_lazy('usuario:usuario_listar')