from django.urls import path, include
from . import views

urlpatterns = [
    path('create_servico/', views.create_servico, name="create_servico"),
    path('index_servico/', views.index_servico, name="index_servico")
  ]