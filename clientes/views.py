from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializers import ClienteSerializer
from django.http import JsonResponse
from .models import Cliente

def get_cliente_por_cpf(request, cpf):
    try:
        cliente = Cliente.objects.get(cpf=cpf)
        data = {
            'cpf': cliente.cpf,
            'nome': cliente.nome,
            'data de nascimento': cliente.data_nasc,
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente não encontrado'}, status=404)

class ArmazenaDadosAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Client saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetiraDadosAPIView(APIView):
    def get(self, request, cpf, *args, **kwargs):
        try:
            cliente = Cliente.objects.get(cpf=cpf)
        except Cliente.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"nome": cliente.nome, "cpf": cliente.cpf,"data de nascimento": cliente.data_nasc}, status=status.HTTP_200_OK)

def home(request):
    return HttpResponse("Bem-vindo à API do Desafio!")
