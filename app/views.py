from django.shortcuts import render
from django.http import HttpResponse
from .forms import TopForm

def top(request):
    params = {
        "nameform": TopForm(),
    }
    return render(request, 'app/top.html', params)

def result(request):
    name = request.POST["name"]
    params = {
        "nameform": TopForm(),
        "name": name,
        "pokemon": pokemon(name),
        "pokename": pokename(name),
    }
    return render(request, 'app/result.html', params)

def pokemon(name):
    x = len(name)
    y = x % 5
    if y == 0:
        pokemon = "https://www.pokemon.jp/zukan/detail/001.html"
    elif y == 1:
        pokemon = "https://www.pokemon.jp/zukan/detail/006.html"
    elif y == 2:
        pokemon = "https://www.pokemon.jp/zukan/detail/011.html"
    elif y == 3:
        pokemon = "https://www.pokemon.jp/zukan/detail/039.html"
    else:
        pokemon = "https://www.pokemon.jp/zukan/detail/383.html"
    return pokemon

def pokename(name):
    i = len(name)
    j = i % 5
    if j == 0:
        pokename = "フシギダネ"
    elif j == 1:
        pokename = "リザードン"
    elif j == 2:
        pokename = "トランセル"
    elif j == 3:
        pokename = "プリン"
    else:
        pokename = "グラードン"
    return pokename