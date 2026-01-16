from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'é necessario efetuar login')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"dados": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'é necessario efetuar login')
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    if 'buscar' in request.GET:
        buscar_a_nome = request.GET['buscar']
        if buscar_a_nome:
            fotografias = fotografias.filter(nome__icontains=buscar_a_nome)

    return render(request, "galeria/buscar.html", {"dados": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'é necessario efetuar login')
        return redirect('login')

    form = FotografiaForms()
    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem cadastrada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {"form": form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass