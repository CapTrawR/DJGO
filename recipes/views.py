from django.shortcuts import render

#from django.shortcuts import render -> este import vai nos ajudar com o html temos que usar
# tenho que fazer os imports necessarios para aqui de acordo com as funcoes
# Create your views here.
# sao as funcoes para as urls
#preciso faazer uma pasta chamada template

def home(request):
    return render(request, 'recipes/pages/home.html');

# def sobre(request):
#     return HttpResponse ('SOBRE') isto era o que tinhamos antes de explicacao

#nova view para outra pagina
def postview(request, id):
    return render(request, 'recipes/pages/post-view.html')