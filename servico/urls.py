from django.urls import path, include
from . import views

urlpatterns = [
    path('create_servico/', views.create_servico, name="create_servico"),
    path('index_servico/', views.index_servico, name="index_servico"),
    path('edit_servico/<int:id>', views.edit_servico, name='edit_servico'),
    path('delete_servico/<int:id>', views.delete_servico, name='delete_servico'),
    path('gerar_pdf/<int:id>', views.gerar_pdf, name='gerar_pdf')
  ]