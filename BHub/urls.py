"""BHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cliente.api.viewsets import ClienteViewsets, BancoViewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema = get_schema_view(
    openapi.Info(
        title='BHub API - Challenge',
        default_version='1.0.0',
        description='API para desafio BHub'
    ),
    public=True,
)

r = routers.DefaultRouter()
r.register('cliente', viewset= ClienteViewsets)
r.register('banco', viewset=BancoViewsets)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(
        [
            path('', include(r.urls)),
            path('swagger/', schema.with_ui('swagger', cache_timeout=0)),
            path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        ]
    ))
]

