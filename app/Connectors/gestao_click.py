import os
import requests
from dotenv import load_dotenv

load_dotenv()

class gestao_click:
    def __init__(self):
        self.url = os.getenv('URL_BASE_GESTAO_CLICK')
        self.header = {
            "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}, {os.getenv('SECRET_ACCSESS_TOKEN')}"
        }
        
    # def  create_product(self, product):
        
        