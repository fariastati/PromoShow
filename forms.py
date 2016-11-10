from django import forms

from apps.usuario.models import Usuario

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario

		fields = [
			'nome',
			'cpf',
			'email',
			'telefone',
			'endereco',
			'cep',
			'estado',
		]
		labels = {
			'nome': 'nome',
			'cpf': 'cpf',
			'email': 'email',
			'telefone': 'telefone',
			'endereco': 'endereco',
			'cep': 'cep',
			'estado': 'estado',	
		}
		widgets = {
			'nome': forms.TextInput(attrs={'class':'form-control'}),
			'cpf': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'telefone': forms.TextInput(attrs={'class':'form-control'}),
			'endereco': forms.TextInput(attrs={'class':'form-control'}),
			'cep': forms.TextInput(attrs={'class':'form-control'}),
			'estado': forms.TextInput(attrs={'class':'form-control'}),
		}