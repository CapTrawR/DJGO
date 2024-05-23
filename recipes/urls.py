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
    path('',views.PostListViewHome.as_view(), name="Home"), # implementar url correctas
    path('Posts/search/', views.PostListViewSearch.as_view(), name = 'search'),
    path('Posts/category/<int:category_id>/', views.PostListViewCategory.as_view(), name="category"),
    path('Posts/<int:pk>/', views.PostDetail.as_view(), name="post"),
]