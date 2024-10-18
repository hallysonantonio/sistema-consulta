from django import forms
from .models import Paciente
from .models import Consulta

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'cpf']

class ConsultasForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['cliente', 'descricao', 'valor']