dic_produtos = {}

for i in range (3):
    
    nome_produto = input ('Digite o nome do produto: ')
    preco_produto = float (input ('Digite o preco do produto: '))

    dic_produtos [nome_produto] = preco_produto

for produto in dic_produtos:

    novo_preco = dic_produtos [produto] * 1.1 #aumento de 10%
    dic_produtos[produto] = novo_preco

print (dic_produtos)