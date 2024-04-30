from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.http.response import Http404
from django.db.models import Q # quero and ou or 
from utils.pagination.pagination import make_pagination

import os

PER_PAGE = int(os.environ.get('PER_PAGE', 6))

#from django.shortcuts import render -> este import vai nos ajudar com o html temos que usar
# tenho que fazer os imports necessarios para aqui de acordo com as funcoes
# Create your views here.
# sao as funcoes para as urls
#preciso faazer uma pasta chamada template

def home(request):
    posts = Post.objects.filter(is_published = True).order_by('-id') # aqui e como eu vou buscar o que eu tenho na BD a fazer is_published = True estou a ir buscar a bd bollean
    
    page_object, pagination_range = make_pagination(request,posts,PER_PAGE)

    return render(request, 'recipes/pages/home.html', context={
        'posts': page_object,
        'pagination_range' : pagination_range,
    })

# def sobre(request):
# esta e a parte das categorias e um filtro por categoria 
def category(request,category_id):
    posts = get_list_or_404(
        Post.objects.filter(
            category__id = category_id, is_published = True,
        ).order_by('-id'))
    
    page_object, pagination_range = make_pagination(request,posts,PER_PAGE)

    return render(request, 'recipes/pages/category.html', context={
        'posts': page_object,
        'pagination_range': pagination_range,
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
    
    posts = Post.objects.filter(
        # isto faz a procura com as letras e nao examtamente igual e um like em sql o i faz com que nao seja case sensitive
        Q(
            Q(title__icontains = search_term) | 
            Q(description__icontains = search_term), # faz o mesmo para descricao
        ),
        is_published = True
    ).order_by('-id')

    page_object, pagination_range = make_pagination(request,posts,PER_PAGE)
    
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}" | ',
        'search_term': search_term,
        'pagination_range': pagination_range,
        'posts':page_object,
        'additional_url_query': f'&q={search_term}',
    })