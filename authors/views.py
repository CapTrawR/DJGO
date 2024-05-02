from django.shortcuts import render
from .forms import RegisterForm
from django.http import Http404
from django.shortcuts import redirect

# se alguem enviar o metodo post o navegador recebe como post passa para dentro do formolario se nao cria um novo
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html',{
      'form': form,
   })

# aqui retorna-nos para o form com os respectivos erros 
def register_create(request):
    if not request.POST:
        raise Http404() #cria me um erro 404
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    
    return redirect('authors:register')