from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"dados": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if 'buscar' in request.GET:
        buscar_a_nome = request.GET['buscar']
        if buscar_a_nome:
            fotografias = fotografias.filter(nome__icontains=buscar_a_nome)

    return render(request, "galeria/buscar.html", {"dados": fotografias})