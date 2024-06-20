''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''
print('-' * 40)
print('{: ^40}'.format('LOJA SUPER BARATÃO'))
print('-' * 40)
compra = qtsproduto1000 = mairo = menor = quant = 0
barato = ' '
while True:
    produto = str(input('Nome do Prodoto: '))
    preco = int(input('Preço: R$'))
    compra += preco
    quant += 1
    pergunta = ' '
    if preco > 1000:
        qtsproduto1000 += 1  
    while pergunta not in 'SN':
        pergunta = str(input('Quer contiuar? [S/N]')).strip() .upper() [0]
    if quant == 1 or preco < menor:
        menor = preco
        barato = produto    
    '''else:
        if preco < menor:
            menor = preco
            barato = produto'''
    if pergunta == 'N':
        break
print(f'Total da compra foi {compra}')
print(f'Temos {qtsproduto1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor}.')