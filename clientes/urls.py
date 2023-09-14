from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('listar/', views.listar, name='listar'),
    path('edit/<int:user_id>', views.edit, name='edit')
  ]