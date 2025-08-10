"""
Arquivo de "Banco de Dados" (database.py)
------------------------------------------
Usei este arquivo para guardar os dados do sistema enquanto ele está rodando.
Funciona como um banco de dados temporário, que fica só na memória.

Entendo que os dados se perdem ao fechar o programa, mas para o escopo
deste projeto, atende ao que foi pedido na atividade.
"""

# Lista que armazena os produtos do cardápio.
# Cada produto é um dicionário.
cardapio = [
    {'id': 1, 'nome': 'Expresso', 'preco': 6.00},
    {'id': 2, 'nome': 'Café Coado', 'preco': 8.00},
    {'id': 3, 'nome': 'Cappuccino Italiano', 'preco': 10.00},
    {'id': 4, 'nome': 'Mocha da Rosa', 'preco': 14.00},
    {'id': 5, 'nome': 'Pão de Queijo (Porção)', 'preco': 9.00},
    {'id': 6, 'nome': 'Bolo de Cenoura', 'preco': 10.00}
    # Adicione mais itens se quiser
]

# Lista para armazenar os clientes cadastrados.
clientes = []

# Lista para armazenar os pedidos feitos.
pedidos = []