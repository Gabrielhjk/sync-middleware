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
    
    def  create_product(self, product):
        product = requests.post(f"{self.url}/produtos", json=product, headers=self.headers)
        return product

    def update_sales(self, product, id):
        product_sales = requests.put(f"{self.url}/vendas/{id}", json=product, headers=self.headers)
        return product_sales

        
        