from django.urls import path
# aqui temos que fazer o import da app 
from recipes import views

'''fazer  o http response'''

'''isto nao vai ficar assim e so para nao dar erro no path
isto e um http request'''
# def _home(request):
#     return HttpResponse ('Home')
'''devia retornar um http response'''
#posts:post isto da para fazer os urls assim
app_name = 'Posts'


urlpatterns= [
    path('',views.home, name="Home"), # implementar url correctas
    path('Posts/search/', views.search, name = 'search'),
    path('Posts/category/<int:category_id>/', views.category, name="category"),
    path('Posts/<int:id>/', views.postview, name="Post"),
]