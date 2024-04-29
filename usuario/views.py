from django.shortcuts import render

# Create your views here.
def usuarios(request):
    if request.method == 'GET':
        return render(request, 'login')