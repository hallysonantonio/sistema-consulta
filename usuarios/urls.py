from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.listar_usuarios, name='lista_usuarios'),
    path('novo', views.criar_usuario, name='criar_usuario'),
    path('editar/<int:pk>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuario'),
    path('exportar_usuarios_pdf/', views.exportar_usuarios_pdf, name='exportar_usuarios_pdf'),

    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    
    # URL para fazer logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
