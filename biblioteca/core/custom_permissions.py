from rest_framework import permissions

class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):
    
    """
    Permissão que permite leitura para todos, mas escrita apenas para o colecionador da coleção.
    """
    def has_object_permission(self, request, view, obj):
        # Permissão total para métodos seguros (leitura: GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permissão de escrita apenas para o colecionador
        else:
            return obj.colecionador == request.user