from django.contrib import admin
from django.urls import path
from clientes.views import ArmazenaDadosAPIView, RetiraDadosAPIView, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('armazena-dados/', ArmazenaDadosAPIView.as_view(), name='armazena_dados'),
    path('retira-dados/<str:cpf>/', RetiraDadosAPIView.as_view(), name='retira_dados'),
    path('', home, name='home'),  # Página inicial
]
