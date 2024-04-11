from django.shortcuts import render
from utils.posts.factory import make_posts

#from django.shortcuts import render -> este import vai nos ajudar com o html temos que usar
# tenho que fazer os imports necessarios para aqui de acordo com as funcoes
# Create your views here.
# sao as funcoes para as urls
#preciso faazer uma pasta chamada template

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'posts': [make_posts()for _ in range (10)]
    })

# def sobre(request):
#     return HttpResponse ('SOBRE') isto era o que tinhamos antes de explicacao

#nova view para outra pagina
def postview(request, id):
    return render(request, 'recipes/pages/post-view.html', context={
        'post': make_posts(),
        'is_detail_page': True,
    })