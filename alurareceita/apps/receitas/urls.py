from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:receita_id>', receita, name='receita' ),
    path('buscar', buscar, name='buscar'),
    path('cria_receita', cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', deleta_receita, name='deleta_receita'),
    path('editar_receita/<int:receita_id>', editar_receita, name='editar_receita'),
    path('atualizar_receita/<int:receita_id>', atualizar_receita, name='atualizar_receita'),
]