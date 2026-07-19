# criar produtos
product = {
    "nome": "Televisão Smart TV - LED 32",
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

# atualizar vendas
product_sale = {
    "tipo": "produto",
    "cliente_id": "60058779",
    "vendedor_id": "1380647",
    "data": "2026-07-19",
    "prazo_entrega": "2026-07-19",
    "situacao_id": "9275087",
    "nome_situacao": "Em andamento",
    "transportadora_id": "",
    "centro_custo_id": "",
    "valor_frete": "5.00",
    "condicao_pagamento": "a_vista",
    "pagamentos": [
        {
            "pagamento": {
                "data_vencimento": "2026-07-19",
                "valor": "562.99",
                "forma_pagamento_id": "6677195",
                "nome_forma_pagamento": "PIX",
                "plano_contas_id": "35984640",
                "nome_plano_conta": "Vendas de produtos",
                "observacao": ""
            }
        }
    ],
    "produtos": [
        {
            "produto": {
                "produto_id": "95651099",
                "variacao_id": "167093999",
                "detalhes": "",
                "quantidade": "1.00",
                "valor_venda": "550.99",
                "tipo_desconto": "R$",
                "desconto_valor": "",
                "desconto_porcentagem": ""
            }
        }
    ],
    "servicos": [
        {
            "servico": {
                "id": "1316689436",
                "servico_id": "95651121",
                "nome_servico": "montar",
                "detalhes": "",
                "sigla_unidade": "",
                "quantidade": "1.00",
                "tipo_valor_id": "",
                "nome_tipo_valor": "",
                "valor_venda": "7.00",
                "tipo_desconto": "R$",
                "desconto_valor": "0",
                "desconto_porcentagem": "0"
            }
        }
    ]
}
