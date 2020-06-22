"""cashback_boticario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login/')),
    path('main/', views.main),
    path('main/cadastroCompra/', views.cadastro_compra),
    path('main/cadastroCompra/submit', views.submit_cadastro_compra),
    path('main/listarCompras/', views.listar_compras),
    path('main/cashback/', views.cashback),
    path('register/', views.cadastro_usuario),
    path('register/submit', views.submit_cadastro_usuario),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
]
