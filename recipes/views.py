from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post
from django.http.response import Http404
from django.db.models import Q # quero and ou or 
from utils.pagination.pagination import make_pagination
from django.views.generic import ListView, DetailView

import os

PER_PAGE = int(os.environ.get('PER_PAGE', 6))

#from django.shortcuts import render -> este import vai nos ajudar com o html temos que usar
# tenho que fazer os imports necessarios para aqui de acordo com as funcoes
# Create your views here.
# sao as funcoes para as urls
#preciso faazer uma pasta chamada template

class PostListViewBase(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = None
    ordering = ['-id']
    template_name = 'recipes/pages/home.html'

    def get_queryset(self,*args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            is_published = True,
        )
        return qs
    
    def get_context_data(self,*args, **kwargs ):
        ctx = super().get_context_data(*args, **kwargs)
        page_object, pagination_range = make_pagination(
            self.request,ctx.get('posts'),
            PER_PAGE
        )
        ctx.update(
            {'posts': page_object, 'pagination_range':pagination_range}
        )
        return ctx

class PostListViewHome(PostListViewBase):
    template_name = 'recipes/pages/home.html'

class PostListViewCategory(PostListViewBase):
    template_name = 'recipes/pages/category.html'

    def get_context_data(self,*args, **kwargs ):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '')
        ctx.update({
            'title':f'{ctx.get("posts")[0].category.name} - Category |'
        })
        return ctx

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
            category__id=self.kwargs.get('category_id')
        )
        return qs
class PostListViewSearch(PostListViewBase):
    template_name = 'recipes/pages/search.html'

    def get_queryset(self,*args, **kwargs):
        search_term =self.request.GET.get('q', '')
        qs = super().get_queryset(*args, **kwargs)
        qs = qs.filter(
        Q(
            Q(title__icontains = search_term) | 
            Q(description__icontains = search_term), # faz o mesmo para descricao
        ),
            is_published = True,
        )
        return qs
    
    def get_context_data(self,*args, **kwargs ):
        ctx = super().get_context_data(*args, **kwargs)
        search_term = self.request.GET.get('q', '')
        ctx.update({
            'page_title': f'Search for "{search_term}" | ',
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        })
        return ctx

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'recipes/pages/post-view.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        ctx.update({
            'is_detail_page': True
        })
        return ctx