from Connectors.gestao_click import GestaoClick

product = {
    "nome": "Televisão Smart TV - LED 367",
    "codigo_interno": "32355564390",
    "codigo_barra": "98412200100",
    "largura": "80",
    "altura": "50",
    "comprimento": "8",
    "ativo": "1",
    "grupo_id": "803218",
    "nome_grupo": "Eletrônicos",
    "descricao": "Televisão Smart TV com wi-fi 32 Polegadas",
    "estoque": "10",
    "valor_custo": "700.62",
    "valor_venda": "850.99",
    "ncm": "11010010",
    "cest": "0100200",
    "peso_liquido": "1,000",
    "peso_bruto": "1,550",
    "valor_aproximado_tributos": "1,00",
    "valor_fixo_pis": "1,0000",
    "valor_fixo_pis_st": "3.00",
    "valor_fixo_confins": "4.00",
    "valor_fixo_confins_st": "6.00",
    "fornecedores": [
      {
        "fornecedor_id": "4743308"
      }
    ]
  }

api = GestaoClick()
# api.get_fornecedor()
# api.get_products()
api.create_product(product)