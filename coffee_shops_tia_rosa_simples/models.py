"""
Arquivo de Modelos (models.py)
------------------------------
Criei este arquivo para definir a estrutura dos meus dados principais,
usando Classes, como foi pedido na atividade.

A classe `Produto` e a `Cliente` servem como um "molde" para garantir
que todos os produtos e clientes do sistema tenham sempre a mesma
estrutura de dados.
"""

class Produto:
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

class Cliente:
    def __init__(self, id_cliente, nome, contato):
        self.id_cliente = id_cliente
        self.nome = nome
        self.contato = contato