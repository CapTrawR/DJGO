from django.urls import path
# aqui temos que fazer o import da app 
from recipes.views import home, contacto, sobre

'''fazer  o http response'''

'''isto nao vai ficar assim e so para nao dar erro no path
isto e um http request'''
# def _home(request):
#     return HttpResponse ('Home')
'''devia retornar um http response'''

urlpatterns = [
    #criar path e assim
    path('', home),#home,
    path('sobre/', sobre),
    path('contacto/', contacto),
]