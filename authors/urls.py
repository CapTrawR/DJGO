from django.urls import path
from . import views


app_name = 'authors'


urlpatterns = [
    path('register/',views.register_view, name="register"),
    path('register/create/',views.register_create, name="register_create"),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/post/<int:id>/edit/', views.dashboard_post_edit, name='dashboard_post_edit'),
    path('dashboard/post/new/', views.dashboard_post_new, name='dashboard_post_new'),
    path('dashboard/post/<int:id>/delete/', views.dashboard_post_delete, name='dashboard_post_delete'),
]
