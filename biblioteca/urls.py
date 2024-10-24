from django.urls import path
from . import views

app_name = 'biblio'

urlpatterns = [    
    path('sobre/',views.view_sobre, name='sobre'),
    path('home/', views.view_home, name='home'),
    path('contato/', views.view_contato, name='contato'),
    path('livros/', views.view_livros, name='livros'),
    path('sobre/livro/<str:id>/', views.view_livro, name='livro'),
]