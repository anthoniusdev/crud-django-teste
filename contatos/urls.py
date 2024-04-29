from django.urls import path
from .views import novoContato
urlpatterns = [
    path('adicionar/', novoContato, name='novoContato')
]
