from django.shortcuts import render, redirect
from .models import Contato
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')
def novoContato(request):
    if request.method == 'GET':
        return render(request, 'novoContato.html')
    elif request.method == 'POST':
        telefone = request.POST.get('fone')
        contato = Contato.objects.filter(telefone=telefone)
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        if contato.exists():
            return render(request, 'novoContato.html', {'email': email,
                                                   'nome': nome,
                                                   'alert': "Este telefone já foi cadastrado"})
        contato = Contato(nome=nome,
                          telefone=telefone,
                          email=email)
        contato.save()
        return redirect('agenda')