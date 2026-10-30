from django.shortcuts import render, redirect, get_object_or_404
from jogoapp.forms import *


# Create your views here.
def index(request):
    jogos = Jogo.objects.all()
    form = JogoForm()
    if request.method == "POST":
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('index')
    context = {
        'form':form ,
        'jogos':jogos
    }
    return render(request, 'jogo/index.html',context)

def teste(request):

    return render(request,'jogo/teste.html')


def editar_index(request, id):
    jogo =get_object_or_404(Jogo, pk=id)
    form = JogoForm(instance=jogo)
    if(request.method =="POST"):
        form =JogoForm(request.POST, request.FILES, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'jogo/editar_index.html', {'jogo':jogo, 'form':form})


    else:
        return render(request, 'jogo/editar_index.html', {'jogo': jogo, 'form': form})


def deletar_jogo(request, id):
        jogo = get_object_or_404(Jogo, pk= id)
        form = JogoForm(instance=jogo)
        if (request.method == "POST"):
            jogo.delete()
            return redirect('index')
        return render(request, 'jogo/deletar_jogo.html', {'jogo':jogo, 'form':form})
