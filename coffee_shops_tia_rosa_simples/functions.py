"""
Arquivo de Funções (functions.py)
---------------------------------
Aqui fica o "cérebro" do sistema. Coloquei todas as funções que
fazem o trabalho de verdade: cadastrar, listar, registrar pedido, etc.

Elas pegam as listas que estão no `database.py` e fazem todas as
manipulações necessárias nos dados.
"""

import os
# Importa as listas do nosso "banco de dados"
from database import cardapio, clientes, pedidos
# Importa as classes que definimos
from models import Produto, Cliente

def limpar_tela():
    """Limpa o console do terminal para melhorar a legibilidade."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Funções de Gerenciamento de Produtos ---

def listar_cardapio():
    """Exibe o cardápio de produtos de forma organizada no console."""
    print("--- Cardápio Coffee Shops Tia Rosa ---")
    if not cardapio:
        print("Cardápio vazio.")
        return
    for item in cardapio:
        print(f"ID: {item.id} | Produto: {item.nome} | Preço: R${item.preco:.2f}")
    print("--------------------------------------")

def adicionar_produto():
    """Solicita os dados de um novo produto ao usuário e o adiciona à base de dados.

    A função pede o nome e o preço, gera um novo ID automaticamente e,
    se os dados forem válidos, cria um novo objeto Produto e o insere na
    lista 'cardapio'.
    """
    print("--- Adicionar Novo Produto ---")
    nome = input("Digite o nome do produto: ")
    while True:
        try:
            preco = float(input("Digite o preço do produto (ex: 12.50): "))
            break
        except ValueError:
            print("[!] Erro: Por favor, digite um número válido para o preço.")
    # Gera o novo ID automaticamente (maior ID + 1)
    if cardapio:
        novo_id = max(item.id for item in cardapio) + 1
    else:
        novo_id = 1
    novo_produto = Produto(novo_id, nome, preco)
    cardapio.append(novo_produto)
    print(f"\n[✓] Produto '{nome}' adicionado com sucesso!")

# --- Funções de Gerenciamento de Clientes ---

def listar_clientes():
    """Exibe a lista de clientes cadastrados.

    Returns:
        bool: Retorna True se houver clientes para listar, False caso contrário.
    """
    print("--- Clientes Cadastrados ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return False
    for cliente in clientes:
        print(f"ID: {cliente.id} | Nome: {cliente.nome} | Contato: {cliente.contato}")
    print("----------------------------")
    return True

def cadastrar_cliente():
    """Solicita os dados de um novo cliente e o cadastra no sistema.

    Pede ao usuário o nome e o contato, gera um ID único para o cliente
    (iniciando em 101) e o salva na lista 'clientes'.
    """
    print("--- Cadastrar Novo Cliente ---")
    nome = input("Digite o nome do cliente: ")
    contato = input("Digite o contato do cliente (email ou telefone): ")
    # Gera o novo ID automaticamente (maior ID + 1, começando em 101 se desejar)
    if clientes:
        novo_id = max(cliente.id for cliente in clientes) + 1
    else:
        novo_id = 101
    novo_cliente = Cliente(novo_id, nome, contato)
    clientes.append(novo_cliente)
    print(f"\n[✓] Cliente '{nome}' cadastrado com sucesso!")

# --- Funções de Pedidos e Relatórios ---

def listar_pedidos_registrados():
    """Exibe um histórico com todos os pedidos que foram finalizados."""
    print("--- Histórico de Pedidos ---")
    if not pedidos:
        print("Nenhum pedido registrado ainda.")
        return
    for pedido in pedidos:
        print(f"Pedido #{pedido['id']} | Cliente: {pedido['nome_cliente']} | Total: R${pedido['total']:.2f}")
        print("Itens:")
        for item in pedido['itens']:
            print(f"  - {item.nome}: R${item.preco:.2f}")
        print("--------------------------------------")

def registrar_pedido():
    """Orquestra o fluxo completo de registro de um novo pedido.

    Esta é a função mais complexa do sistema. Ela executa os seguintes passos:
    1. Verifica se existem clientes e produtos cadastrados.
    2. Permite a seleção de um cliente válido.
    3. Inicia um loop para adicionar produtos do cardápio ao pedido.
    4. Após a finalização, calcula o valor total.
    5. Gera um ID para o novo pedido e o salva na lista 'pedidos'.
    6. Exibe um resumo completo do pedido registrado.
    """
    print("--- Registrar Novo Pedido ---")
    if not cardapio or not clientes:
        print("[!] É necessário ter ao menos um produto no cardápio e um cliente cadastrado.")
        return

    listar_clientes()
    cliente_selecionado = None
    while cliente_selecionado is None:
        try:
            cliente_id = int(input("Digite o ID do cliente para o pedido: "))
            for cliente in clientes:
                if cliente.id == cliente_id:
                    cliente_selecionado = cliente
                    break
            if cliente_selecionado is None:
                print("[!] ID de cliente não encontrado. Tente novamente.")
        except ValueError:
            print("[!] Erro: Por favor, digite um número inteiro para o ID.")

    limpar_tela()
    print(f"[✓] Cliente selecionado: {cliente_selecionado.nome}")
    print("--------------------------------------")
    
    itens_do_pedido = []
    while True:
        listar_cardapio()
        id_produto_str = input("Digite o ID do produto para adicionar ou [0] para finalizar o pedido: ")
        if id_produto_str == '0':
            if not itens_do_pedido:
                print("[!] Nenhum produto foi adicionado. Pedido cancelado.")
                return
            break
        try:
            id_produto = int(id_produto_str)
            produto_encontrado = None
            for produto in cardapio:
                if produto.id == id_produto:
                    produto_encontrado = produto
                    break
            if produto_encontrado:
                itens_do_pedido.append(produto_encontrado)
                print(f"\n[✓] '{produto_encontrado.nome}' foi adicionado ao pedido.")
            else:
                print(f"\n[!] Produto com ID {id_produto} não encontrado no cardápio.")
        except ValueError:
            print("\n[!] Entrada inválida. Por favor, digite um número de ID.")
        
        input("\nPressione Enter para continuar...")
        limpar_tela()
        print(f"Pedido para: {cliente_selecionado.nome}")
        print("Itens atuais:", ", ".join([item.nome for item in itens_do_pedido]))
        print("--------------------------------------")

    valor_total = sum(item.preco for item in itens_do_pedido)
    novo_pedido_id = (pedidos[-1]['id'] + 1) if pedidos else 1
    novo_pedido = {
        'id': novo_pedido_id,
        'id_cliente': cliente_selecionado.id,
        'nome_cliente': cliente_selecionado.nome,
        'itens': itens_do_pedido,
        'total': valor_total
    }
    pedidos.append(novo_pedido)
    limpar_tela()
    print("==========================================")
    print("         [✓] Pedido Registrado com Sucesso!         ")
    print("==========================================")
    print(f"ID do Pedido: {novo_pedido['id']}")
    print(f"Cliente: {novo_pedido['nome_cliente']}")
    print("\nItens:")
    for item in novo_pedido['itens']:
        print(f"  - {item.nome}: R${item.preco:.2f}")
    print("------------------------------------------")
    print(f"VALOR TOTAL: R${novo_pedido['total']:.2f}")
    print("==========================================")
    input("Pressione Enter para voltar ao menu principal...")