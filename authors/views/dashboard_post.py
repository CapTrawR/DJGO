from urllib import request
from django.http import Http404
from django.views import View
from django.contrib import messages
from authors.forms.post_form import AuthorPostForm
from authors import *
from django.shortcuts import redirect,render
from django.urls import reverse
from recipes.models import Post

class DashboardPost(View):
    # vai me buscar o post especifico 
    def get_post(self, id):
        post = None
        if id:
            post = Post.objects.filter(
                is_published=False,
                author = self.request.user,
                pk=id,
            ).first()

            if not post:
                raise Http404()


        return post

    #mete me o post a ser visto
    def render_post(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_post.html',
            context={
                'form': form,
                
            }
        )
    
    def get(self,request, id):
        post=self.get_post(id)
        form=AuthorPostForm(instance=post)
        return self.render_post(form)
    
    
    def post(self, request, id):
        post = self.get_post(id)
        form = AuthorPostForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance = post
            )
        
        if form.is_valid():
        #agora o form e valido eu posso tentar gravar
            post = form.save(commit=False) # finge que guarda mas mete num variavel!!

        # aqui faço as minhas validacoes
            post.speciality = form.cleaned_data['speciality']
            post.author = request.user
            post.post_field_is_html = False
            post.is_published = False

        # aqui gravo mesmo na base de dados
            post.save()

            messages.success(request, 'Your post have been edit successfully')
            return redirect(reverse('authors:dashboard_post_edit', args=(id,)))

        return self.render_post(form)