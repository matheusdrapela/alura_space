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

    return render(request, "galeria/index.html", {"dados": fotografias})

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

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == "POST":
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem atualizada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {"form": form, "foto_id": foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(pk=foto_id)
    fotografia.delete()
    messages.success(request, 'Imagem deletada com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)

    return render(request, 'galeria/index.html', {"dados": fotografias})