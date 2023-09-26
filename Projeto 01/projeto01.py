#Importando o módulo json para lidar com a leitura e gravação de dados em formato JSON.
import json

# Tentando abrir o arquivo "produtos.json" para carregar os dados dos produtos. 

try:
    with open("produtos.json", "r") as arquivo:
        produtos = json.load(arquivo)
except FileNotFoundError:
    produtos = {}

# Função para salvar os dados dos produtos no arquivo JSON
def salvar_produtos():
    with open("produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)

# Função para inserir um novo produto
def inserir_produto():
    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        print("Este código de produto já existe.")
        return

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    disponivel = True if input("O produto está disponível? (S/N): ").lower() == "s" else False

    produtos[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "disponivel": disponivel
    }
    salvar_produtos()
    print("Produto adicionado com sucesso!")

# Função para consultar um produto por código
def consultar_produto():
    codigo = input("Digite o código do produto: ")
    produto = produtos.get(codigo)
    if produto:
        print("Informações do produto:")
        print(f"Código: {codigo}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}")
        print(f"Disponível: {'Sim' if produto['disponivel'] else 'Não'}")
    else:
        print("Produto não encontrado.")

# Função para listar todos os produtos
def listar_produtos():
    for codigo, produto in produtos.items():
        print(f"Código: {codigo}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Quantidade em estoque: {produto['quantidade']}")
        print(f"Disponível: {'Sim' if produto['disponivel'] else 'Não'}")
        print()

# Função para alterar o preço de um produto
def alterar_preco():
    codigo = input("Digite o código do produto: ")
    produto = produtos.get(codigo)
    if produto:
        novo_preco = float(input("Digite o novo preço do produto: "))
        produto['preco'] = novo_preco
        salvar_produtos()
        print("Preço atualizado com sucesso!")
    else:
        print("Produto não encontrado.")

# Função para aplicar acréscimo ou desconto em todos os produtos
def aplicar_acrescimo_desconto():
    percentual = float(input("Digite o percentual (positivo para acréscimo, negativo para desconto): "))
    for produto in produtos.values():
        produto['preco'] *= (1 + percentual / 100)
    salvar_produtos()
    print("Acréscimo ou desconto aplicado com sucesso!")

# Função para excluir um produto
def excluir_produto():
    codigo = input("Digite o código do produto que deseja excluir: ")
    if codigo in produtos:
        del produtos[codigo]
        salvar_produtos()
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")

# Loop principal do programa
while True:
    print("\nMenu de Opções:")
    print("1. Inserir um novo produto")
    print("2. Consultar um produto por código")
    print("3. Consultar todos os produtos")
    print("4. Alterar o preço de um determinado produto")
    print("5. Aplicar um acréscimo ou desconto em todos os produtos")
    print("6. Excluir um registro de produto")
    print("7. Sair do programa")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        inserir_produto()
    elif opcao == "2":
        consultar_produto()
    elif opcao == "3":
        listar_produtos()
    elif opcao == "4":
        alterar_preco()
    elif opcao == "5":
        aplicar_acrescimo_desconto()
    elif opcao == "6":
        excluir_produto()
    elif opcao == "7":
        print("Encerrando o programa. Salvando alterações...")
        salvar_produtos()
        break
    else:
        print("Opção inválida. Tente novamente.")
