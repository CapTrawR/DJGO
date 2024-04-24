from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.http.response import Http404


#from django.shortcuts import render -> este import vai nos ajudar com o html temos que usar
# tenho que fazer os imports necessarios para aqui de acordo com as funcoes
# Create your views here.
# sao as funcoes para as urls
#preciso faazer uma pasta chamada template

def home(request):
    posts = Post.objects.filter(is_published = True).order_by('-id') # aqui e como eu vou buscar o que eu tenho na BD a fazer is_published = True estou a ir buscar a bd bollean
    return render(request, 'recipes/pages/home.html', context={
        'posts': posts,
    })

# def sobre(request):
# esta e a parte das categorias e um filtro por categoria 
def category(request,category_id):
    posts = get_list_or_404(
        Post.objects.filter(
            category__id = category_id, is_published = True,
        ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'posts': posts,
        'title':f'{posts[0].category.name} - Category |'
    })

#nova view para outra pagina
def postview(request, id):
    posts = get_object_or_404(Post,id = id, is_published = True,)
    return render(request, 'recipes/pages/post-view.html', context={
        'post': posts,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()  # este q e o que temos no html como variavel para search no input e o espaço strip corta os epaços do direito e esquerdo
    
    if not search_term:
        raise Http404()
    
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" | ',
    })