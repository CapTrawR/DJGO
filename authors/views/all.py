from authors.forms.post_form import AuthorPostForm
from authors.forms import RegisterForm, LoginForm
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.models import Post


# se alguem enviar o metodo post o navegador recebe como post passa para dentro do formolario se nao cria um novo
def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html',{
      'form': form,
      'form_action': reverse('authors:register_create'),
   })

# aqui retorna-nos para o form com os respectivos erros 
def register_create(request):
    if not request.POST:
        raise Http404() #cria me um erro 404
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    # se for valid
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password) # criptografar a password
        user.save()# guarda a senha criptografada na base de dados
        messages.success(request, 'Your user is created, please log in.')

        del(request.session['register_form_data'])
        return redirect(reverse('authors:login'))
    
    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html',{
        'form': form,
        'form_action':reverse('authors:login_create'),
    })


def login_create(request):
    if not request.POST:
        raise Http404() #cria me um erro 404.
    

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username = form.cleaned_data.get('username', ''),
            password = form.cleaned_data.get('password', '')
        )

        if authenticated_user is not None:
            messages.success(request, 'You are logged in')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid Username our Password')
        

    return redirect(reverse('authors:dashboard'))

#uma pessoa que nao esta logada nao pode ter acesso a pagina temos que usar o login decorated
#funcao do logout cuidado para nao dar os mesmo nomes! ficamos com erros de recursao!!
@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):

    # protecao tem que ser um post com csrf token e ser um form e nao um link
    if not request.POST:
        return redirect(reverse('authors:login'))
    
    #pretecao 2 tem que ser p usuario que esta logado a deslogar 
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('authors:login'))
    
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect(reverse('authors:login'))


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    posts = Post.objects.filter(
        is_published = False, # o post nao pode estar publicado
        author=request.user # o user tem que ser o autor do post
    )
    return render(
        request, 'authors/pages/dashboard.html', 
        context={
            'posts':posts
        }
    )

# aqui criamos novos posts
@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_post_new(request):
    form = AuthorPostForm(
        data=request.POST or None,
        files=request.FILES or None,
    )

    if form.is_valid():
        post = form.save(commit=False)
        
        post.speciality = form.cleaned_data['speciality']
        post.author = request.user
        post.post_field_is_html = False
        post.is_published = False

        post.save()

        messages.success(request, 'Your Post have been successfully saved in our database!')
        return redirect(
            reverse('authors:dashboard_post_edit', args=(post.id,))
        )

    return render(
        request,
        'authors/pages/dashboard_post_new.html', # aqui leva me para a pagina html que eu quero
        context={
            'form': form,
            'form_action': reverse('authors:dashboard_post_new')
        }
    )

#
@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_post_delete(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    id = POST.get('id')
    
    post = Post.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    post.delete()
    messages.success(request, 'Deleted successfully.')
    return redirect(reverse('authors:dashboard'))