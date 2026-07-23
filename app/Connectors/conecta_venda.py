from dotenv import load_dotenv
import requests
import os

load_dotenv()

class conecta_venda:
    def __init__(self):
        self.url = os.getenv('')