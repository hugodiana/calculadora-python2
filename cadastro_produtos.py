estoque_produtos = {}

print("Bem-vindo ao Sistema de Estoque!")

while True:
    print("\n--- Menu de Opções ---")
    print("1. Adicionar/Atualizar Produto")
    print("2. Ver Detalhes do Produto")
    print("3. Ver Estoque Completo")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    opcao_int = int(opcao)
    if opcao_int == 1:
        print("\n--- Adicionar/Atualizar Produto ---")
        nome_produto = input("Digite o nome do produto: ")
        try:
            preco = float(input("Digite o preço do produto:"))
            quantidade = int(input("Digite a quantidade em estoque:"))
        except ValueError:
            print("Erro: Preço ou quantidade inválidos. Tente novamente.")
            continue
        detalhes_produto = {
            "preco": preco,
            "quantidade": quantidade
        }
        estoque_produtos[nome_produto] = detalhes_produto
        print(f"Produto '{nome_produto}' adicionado/atualizado com sucesso!")

    elif opcao_int == 2:
        print("\n--- Ver Detalhes do Produto ---")
        nome_consulta = input("Digite o nome do produto para consultar:")
        if nome_consulta in estoque_produtos:
            detalhes = estoque_produtos[nome_consulta]
            print(f"\nDetalhes de '{nome_consulta}':")
            print(f"    Preço: R${detalhes['preco']:.2f}")
            print(f"    Quantidade em estoque: {detalhes['quantidade']}")
        else:
            print(f"Produto '{nome_consulta}' não encontrado no estoque.")

    elif opcao_int == 3:
        print("\n--- Ver Estoque Completo ---")
        if not estoque_produtos:
            print("O estoque está vazio.")
        else:
            print("Produtos no estoque:")
            for nome, detalhes in estoque_produtos.items():
                print(f"- {nome}:")
                print(f"  Preço: R${detalhes['preco']:.2f}")
                print(f"  Quantidade em estoque: {detalhes['quantidade']}")
    elif opcao_int == 4:
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")
1        