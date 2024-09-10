from django.contrib import admin
from django.urls import path
from clientes.views import ArmazenaDadosAPIView, RetiraDadosAPIView, home
from clientes.views import get_cliente_por_cpf
from clientes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cliente/', ArmazenaDadosAPIView.as_view(), name='armazena_dados'),  # Altere a rota aqui
    path('api/cliente/<str:cpf>/', RetiraDadosAPIView.as_view(), name='retira_dados'),  # Altere a rota aqui
    path('', home, name='home'),  # Página inicial
    path('retira-dados/<str:cpf>/', get_cliente_por_cpf, name='retira-dados'),
]
