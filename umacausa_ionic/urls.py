from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('usuarios.urls')),  # URLs do app de usuários
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),  # URLs de autenticação do Django REST Framework
]
