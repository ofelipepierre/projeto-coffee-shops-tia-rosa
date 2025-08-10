# Arquivo: main.py

# Usamos 'as fn' para dar um "apelido" ao nome do arquivo, facilitando a chamada
import functions as fn

def main():
    while True:
        
        fn.limpar_tela() 
        print("==========================================")
        print("   Sistema do Coffee Shops Tia Rosa")
        print("==========================================")
        print("\nEscolha uma opção:")
        print("  1. Ver Cardápio")
        print("  2. Adicionar Produto ao Cardápio")
        print("  3. Cadastrar Novo Cliente")
        print("  4. Listar Clientes Cadastrados")
        print("  5. Registrar Novo Pedido")
        print("\n  0. Sair do Sistema")
        print("==========================================")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            fn.limpar_tela()
            fn.listar_cardapio()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '2':
            fn.limpar_tela()
            fn.adicionar_produto()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '3':
            fn.limpar_tela()
            fn.cadastrar_cliente()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '4':
            fn.limpar_tela()
            fn.listar_clientes()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '5':
            fn.registrar_pedido()
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == '0':
            fn.limpar_tela()
            print("Obrigado por usar o sistema!")
            break
        else:
            print("\n[!] Opção inválida.")
            input("\nPressione Enter para tentar novamente...")

# A parte que inicia o programa não muda.
if __name__ == "__main__":
    main()