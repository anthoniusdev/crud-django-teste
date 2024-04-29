from django.shortcuts import render
from contatos.models import Contato

# Create your views here.
def agendaView(request):
    contatos = Contato.objects.all()
    return render(request, 'agenda.html', {'contatos': contatos})