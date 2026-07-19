import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GestaoClick:
    def __init__(self):
        self.url = os.getenv('URL_BASE_GESTAO_CLICK')
        self.headers = {
            "access-token": f"{os.getenv('ACCESS_TOKEN')}",
            "secret-access-token": f"{os.getenv('SECRET_ACCSESS_TOKEN')}"
        }
    
    
    def get_fornecedor(self):
        response = requests.get(f"{self.url}/fornecedores", headers=self.headers)
        print(response.json())

    # testando conexao para puxar produtos
    def get_products(self):
        response = requests.get(f"{self.url}/produtos", headers=self.headers)
        print(response.json())

    # teste para criar produto
    def  create_product(self, product):
        product = requests.post(f"{self.url}/produtos", json=product, headers=self.headers)
        return product
        
        