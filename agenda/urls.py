from django.urls import path
from .views import agendaView
urlpatterns = [
    path('', agendaView, name='agenda'),
]
