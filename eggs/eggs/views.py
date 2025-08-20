from django.shortcuts import render

def pagina_inicio(request):
    return render(request, 'inicio.html')
