# 1 – Crie um programa em Python que faça o cadastro de algum produto. O cadastro deve conter as seguintes informações: nome do produto, quantidade e preço.
# O cadastro deve ser encerrado quando o usuário digitar “0” no nome do produto.
# Ao final do cadastro mostre os itens cadastrados, o total em estoque por item e o valor total do estoque.
# Criando um dicionário:
perifericos = {}
cont = 1
while True:
    produto = input(f"Digite o nome do {cont}° produto:")
    if (produto == "0"):
        break #print(f"Cadastro finalizado")
        # Realizando input() no dicionário:
    qtde = int(input(f"Digite a quantidade do 1° {produto}:"))
    valor = float(input(f"Digite o valor do 1° {produto}:"))
    # Adicionando elemento no dicionário:
    # perifericos.update({produto: [qtde, valor]}) troquei essa linha por essa:
    perifericos[produto] = {'qtd': qtde,'valor': valor} 
    cont = cont + 1

# Mostrando produtos cadastrados em tela e o valor total dos produtos
qtdetotal = 0
valortotal = 0

#Mostrando quantidade de produtos cadastrados

for produto,periferico in perifericos.items():
    valor_total_prod = periferico['qtd'] * periferico['valor']
    qtde_total_prod = periferico['qtd'] 
    print(f"{produto:10} | QTDE: {periferico['qtd']} | Valor: { periferico['valor']}")
    
    valortotal += valor_total_prod
    qtdetotal += qtde_total_prod 

print(f"\nTotal dos produtos: R${valortotal:,.2f} e Quantidade total: {qtdetotal}")
print(f"Qtde total de produtos cadastrados: {len(perifericos)}")


#2 – Crie um programa que receba dois valores para cálculo de uma exponenciação.
#O primeiro valor será a base e o segundo valor a quantidade de repetições.
#Para cada repetição a seguinte fórmula será executada: x = x + base^2.
#Mostre, a cada repetição, o valor de x. A repetição deve ser feita usando o comando while.

vlr = float(input("Digite o valor da base: "))
qtdrepeticoes = int(input("Digite o número de repetições: "))

vlrini = 0
cont = 1

while cont <= qtdrepeticoes:
    vlrini = vlrini + vlr ** 2
    print(f"Repetição {cont}: Valor = {vlrini}")
    cont += 1


# Criando dicionário vazio:
valor = {}

# input de dados:
vlr = float(input(f"Digite o valor de {valor}:"))
qtdrepeticoes = int(input(f"Digite a quantidade de {modelo}:"))

