from django.urls import path
from .views import novoContato, editarContato, excluirContato
urlpatterns = [
    path('adicionar/', novoContato, name='novoContato'),
    path('editar/<int:idContato>/', editarContato, name='editarContato'),
    path('excluir/<int:idContato>/', excluirContato, name='excluirContato')
]
