from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    nb = models.CharField(max_length=20, blank=True, null=True)  # Defina como opcional
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()

    def __str__(self):
        return self.nome #depois preciso alterar

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='contratos', on_delete=models.CASCADE)
    id_contrato = models.CharField(max_length=50)
    valor = models.FloatField()
    parcelas = models.IntegerField()
    taxa = models.FloatField()
    parcelas_pagas = models.IntegerField()

    def __str__(self):
        return self.id_contrato

class Endereco(models.Model):
    cliente = models.OneToOneField(Cliente, related_name='endereco', on_delete=models.CASCADE)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}'

class Telefone(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='telefones', on_delete=models.CASCADE)
    ddd = models.CharField(max_length=2)
    tel = models.CharField(max_length=9)

    def __str__(self):
        return f'({self.ddd}) {self.tel}'

class Cotacao(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='cotacoes', on_delete=models.CASCADE)
    codigo = models.CharField(max_length=10)
    preco = models.FloatField()
    variacao = models.FloatField()
    abertura = models.FloatField()
    fechamento = models.FloatField()
    horario = models.CharField(max_length=5)
    data = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.codigo} - {self.preco}'