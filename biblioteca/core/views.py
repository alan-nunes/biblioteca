from .serializers import LivroSerializer, AutorSerializer, CategoriaSerializer
from .models import Autor,  Categoria, Livro

from rest_framework import generics

from .filters import LivroFilter

from rest_framework.throttling import ScopedRateThrottle

from rest_framework import permissions
from core import custom_permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class LivroList(generics.ListCreateAPIView):
    throttle_scope = "livros"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    search_fields = ("^titulo")
    ordering_fields = ["titulo", "autor", "categoria", "publicado_em"]
    name = "livro-list"
    
    def perform_create(self, serializer):
        serializer.save()(owner=self.request.user)
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = "livros"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )
    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ("^name")
    name = "categoria-list"
    
class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"