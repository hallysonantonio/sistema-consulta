from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import PacienteForm
from .models import Consultas
from .forms import ConsultasForm
from weasyprint import HTML
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def listar_Pacientes(request):
    Pacientes = Paciente.objects.all()
    return render(request, 'Pacientes/listar_pacientes.html', {'pacientes': Paciente})


def criar_Paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_Paciente')

    else:
        form = PacienteForm()
    return render(request, 'Paciente/criar_Paciente.html', {'form': form})


def atualizar_Paciente(request, id):
    Paciente = get_object_or_404(Paciente, id=id)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=Paciente)
        if form.is_valid():
            form.save()
            return redirect('listar_Paciente')
    else:
        form = PacienteForm(instance=Paciente)
    return render(request, 'Paciente/atualizar_Paciente.html', {'form': form})


def deletar_Paciente(request, id):
    Paciente = get_object_or_404(Paciente, id=id)
    if request.method == "POST":
        Paciente.delete()
        return redirect('listar_Paciente')
    return render(request, 'Paciente/deletar_Paciente.html', {'Paciente': Paciente})


def listar_Consultas(request):
    Consultas = Consultas.objects.all()
    return render(request, 'Consultas/listar_Consultas.html', {'Consultas': Consultas})


def criar_Consultas(request):
    if request.method == "POST":
        form = ConsultasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_Consultas')
    else:
        form = ConsultasForm()
    return render(request, 'Consultas/criar_Consultas.html', {'form': form})


def atualizar_Consultas(request, id):
    Consultas = get_object_or_404(Consultas, id=id)
    if request.method == "POST":
        form = ConsultasForm(request.POST, instance=Consultas)
        if form.is_valid():
            form.save()
            return redirect('listar_Consultas')
    else:
        form = ConsultasForm(instance=Consultas)
    return render(request, 'Consultas/atualizar_Consultas.html', {'form': form})


def deletar_Consultas(request, id):
    Consultass = get_object_or_404(Consultass, id=id)
    if request.method == "POST":
        Consultass.delete()
        # Redireciona para a lista de Consultass
        return redirect('listar_Consultas')
    return render(request, 'Consultas/deletar_Consultas.html', {'Consultas': Consultas})

def exportar_Paciente_pdf(request):
    # Buscando todos os usuários
    Paciente = Paciente.objects.all()

    # Renderizando o template HTML com os dados dos usuários
    html_string = render_to_string('Paciente/Paciente_pdf.html', {'Paciente': Paciente})

    # Criando a resposta HTTP para o PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Paciente.pdf"'

    # Convertendo o HTML para PDF usando WeasyPrint
    HTML(string=html_string).write_pdf(response)

    return response