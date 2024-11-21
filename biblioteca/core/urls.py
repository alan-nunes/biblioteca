from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter

app_name = 'api'

#router = SimpleRouter()
urlpatterns = [
    
    path("livros/", views.LivroList.as_view(), name="livro-list"),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name=views.LivroDetail.name),
    
    path("autores/", views.AutorList.as_view(), name="autor-list"),
    path("autor/<int:pk>/", views.AutorDetail.as_view, name="autor-list"),
    
    path("categorias/", views.CategoriaList.as_view(), name="categoria-list"),
    path("categoria/<int:pk>/", views.CategoriaDetail.as_view(), name="categoria-detail"),
    
    path("colecao/", views.ColecaoListCreate.as_view(), name="colecao-list"),
    path("colecao/<int:pk>/", views.ColecaoDetail.as_view(), name="colecao-detail"),
]