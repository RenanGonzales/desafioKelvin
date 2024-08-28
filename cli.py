import os
import django
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configure o ambiente do Django antes de importar qualquer módulo Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desafioRenan.settings')  # Substitua 'desafioRenan' pelo nome correto do diretório onde está o settings.py
django.setup()

from clientes.models import Cliente, Cotacao


class Scraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")  # Executa o navegador em segundo plano
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    def fetch_data(self):
        self.driver.get("https://www.infomoney.com.br/cotacoes/b3/indice/ibovespa/")
        
        # Rolar a página até o botão "Altas"
        altas_button = self.driver.find_element(By.ID, "high")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", altas_button)

        # Espera explícita até que o botão seja clicável
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "high")))

        # Usar JavaScript para clicar no botão "Altas"
        self.driver.execute_script("arguments[0].click();", altas_button)

        # Esperar o carregamento da tabela de altas
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#high_wrapper tbody tr")))

        # Extrair os dados da tabela de altas
        rows = self.driver.find_elements(By.CSS_SELECTOR, "#high_wrapper tbody tr")
        altas_data = [row.text.split() for row in rows]

        self.driver.quit()
        return altas_data

class DataExporter:
    def __init__(self, filename: str):
        self.filename = filename

    def export_to_csv(self, altas_data):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Código", "Preço", "Variação", "Abertura", "Fechamento", "Horário", "Data"])
            for alta in altas_data:
                writer.writerow(alta)

def save_data_to_db(cpf, altas_data):
    # Busca o cliente pelo CPF
    try:
        cliente = Cliente.objects.get(cpf=cpf)
    except Cliente.DoesNotExist:
        print(f'Cliente com CPF {cpf} não encontrado.')
        return

    # Salva cada cotação no banco de dados
    for cotacao_data in altas_data:
        Cotacao.objects.create(
            cliente=cliente,
            codigo=cotacao_data[0],
            preco=float(cotacao_data[1].replace(',', '.')),
            variacao=float(cotacao_data[2].replace(',', '.')),
            abertura=float(cotacao_data[3].replace(',', '.')),
            fechamento=float(cotacao_data[4].replace(',', '.')),
            horario=cotacao_data[5],
            data=cotacao_data[6]
        )

    print(f'Todas as cotações foram salvas no banco de dados para o cliente {cliente.nome}.')

def main(cpf, output_file):
    scraper = Scraper()
    altas_data = scraper.fetch_data()

    # Salva os dados extraídos no banco de dados
    save_data_to_db(cpf, altas_data)

    # Exporta os dados para CSV
    exporter = DataExporter(filename=output_file)
    exporter.export_to_csv(altas_data)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python cli.py <cpf> <output_file>")
        sys.exit(1)

    cpf = sys.argv[1]
    output_file = sys.argv[2]
    main(cpf, output_file)
