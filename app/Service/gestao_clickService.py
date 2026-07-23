from Connectors.gestao_click import gestao_click

class gestao_click_service:
    def __init__(self):
        self.api = gestao_click()

    def listar(self):
        print(self.api.get_products())