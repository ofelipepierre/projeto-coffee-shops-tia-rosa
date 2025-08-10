# Importa as listas do nosso "banco de dados"
from database import cardapio, clientes, pedidos
# Importa as classes que definimos
from models import Produto, Cliente

def listar_cardapio():
    """Função para exibir o cardápio de forma organizada."""
    print("--- Cardápio Coffee Shops Tia Rosa ---")
    if not cardapio:
        print("Cardápio vazio.")
        return

    for item in cardapio:
        print(f"ID: {item['id']} | Produto: {item['nome']} | Preço: R${item['preco']:.2f}")
    print("--------------------------------------")

def adicionar_produto():
    """Adiciona um novo produto ao cardápio."""
    print("--- Adicionar Novo Produto ---")
    nome = input("Digite o nome do produto: ")
    
    while True:
        try:
            preco = float(input("Digite o preço do produto (ex: 12.50): "))
            break
        except ValueError:
            print("[!] Erro: Por favor, digite um número válido para o preço.")

    # Gera o novo ID de forma segura
    if cardapio:
        novo_id = max(item['id'] for item in cardapio) + 1
    else:
        novo_id = 1

    novo_produto = {
        'id': novo_id,
        'nome': nome,
        'preco': preco
    }
    
    cardapio.append(novo_produto)
    print(f"\n[✓] Produto '{nome}' adicionado com sucesso!")

def cadastrar_cliente():
    """Cadastra um novo cliente no sistema."""
    print("--- Cadastrar Novo Cliente ---")
    nome = input("Digite o nome do cliente: ")
    contato = input("Digite o contato do cliente (email ou telefone): ")

    # Lógica para gerar um novo ID de cliente
    if clientes:
        novo_id = clientes[-1]['id'] + 1
    else:
        novo_id = 1
    
    novo_cliente = {
        'id': novo_id,
        'nome': nome,
        'contato': contato
    }

    clientes.append(novo_cliente)
    print(f"\n[✓] Cliente '{nome}' cadastrado com sucesso!")

def listar_clientes():
    """Exibe a lista de clientes cadastrados."""
    print("--- Clientes Cadastrados ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for cliente in clientes:
        print(f"ID: {cliente['id']} | Nome: {cliente['nome']} | Contato: {cliente['contato']}")
    print("----------------------------")

def registrar_pedido():
    """Registra um novo pedido associando um cliente a produtos do cardápio."""
    print("--- Registrar Novo Pedido ---")

    # 1. Verificações iniciais
    if not cardapio or not clientes:
        print("[!] É necessário ter ao menos um produto no cardápio e um cliente cadastrado.")
        return

    # 2. Seleção do Cliente
    listar_clientes()
    cliente_selecionado = None
    while cliente_selecionado is None:
        try:
            cliente_id = int(input("Digite o ID do cliente para o pedido: "))
            for cliente in clientes:
                if cliente['id'] == cliente_id:
                    cliente_selecionado = cliente
                    break
            if cliente_selecionado is None:
                print("[!] ID de cliente não encontrado. Tente novamente.")
        except ValueError:
            print("[!] Erro: Por favor, digite um número inteiro para o ID.")

    limpar_tela()
    print(f"[✓] Cliente selecionado: {cliente_selecionado['nome']}")
    print("--------------------------------------")
    
    # --- LÓGICA DO CARRINHO DE COMPRAS ---
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
                if produto['id'] == id_produto:
                    produto_encontrado = produto
                    break
            if produto_encontrado:
                itens_do_pedido.append(produto_encontrado)
                print(f"\n[✓] '{produto_encontrado['nome']}' foi adicionado ao pedido.")
            else:
                print(f"\n[!] Produto com ID {id_produto} não encontrado no cardápio.")
        except ValueError:
            print("\n[!] Entrada inválida. Por favor, digite um número de ID.")
        
        input("\nPressione Enter para continuar...")
        limpar_tela()
        print(f"Pedido para: {cliente_selecionado['nome']}")
        print("Itens atuais:", ", ".join([item['nome'] for item in itens_do_pedido]))
        print("--------------------------------------")

    # --- LÓGICA DE FINALIZAÇÃO E SALVAMENTO ---
    valor_total = sum(item['preco'] for item in itens_do_pedido)
    novo_pedido_id = (pedidos[-1]['id'] + 1) if pedidos else 1
    novo_pedido = {
        'id': novo_pedido_id,
        'id_cliente': cliente_selecionado['id'],
        'nome_cliente': cliente_selecionado['nome'],
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
        print(f"  - {item['nome']}: R${item['preco']:.2f}")
    print("------------------------------------------")
    print(f"VALOR TOTAL: R${novo_pedido['total']:.2f}")
    print("==========================================")
    input("Pressione Enter para voltar ao menu principal...")

def limpar_tela():
    """Limpa a tela do terminal de forma multiplataforma."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')