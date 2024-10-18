from django.urls import path
from .import views

urlpatterns = [
    path('', views.listar_pacientes, name='listar_pacientes'),
    path('novo', views.criar_pacientes, name='criar_pacientes'),
    path('editar/<int:id>/', views.atualizar_paciente, name='atualizar_paciente'),
    path('deletar/<int:id>/', views.deletar_paciente, name='deletar_paciente'),
    path('exportar_pacientes_pdf/', views.exportar_clientes_pdf, name='exportar_pacientes_pdf'),

    path('consulta', views.listar_consulta, name='listar_consulta'),
    path('consulta/novo/', views.criar_consulta, name='criar_consulta'),
    path('consulta/editar/<int:id>/', views.atualizar_consulta, name='atualizar_consulta'),
    path('consulta/deletar/<int:id>/', views.deletar_consulta, name='deletar_consulta'),
]
