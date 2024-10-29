from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status

from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from .models import Autor,  Categoria, Livro

from rest_framework.decorators import api_view

from rest_framework import generics

from .filters import LivroFilter

from rest_framework.throttling import ScopedRateThrottle

# Create your views here.
class LivroList(generics.ListCreateAPIView):
    throttle_scope = "livros"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    search_fields = ("^name")
    ordering_fields = ["titulo", "autor", "categoria", "publicado_em"]
    name = "livro-list"

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = "livros"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"
    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^name")
    name = "categoria-list"
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"