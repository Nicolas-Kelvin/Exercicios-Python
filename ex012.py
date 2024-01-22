#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o preço de um produto R$ '))
desc = p * 5 / 100
print('Preço do produto com 5% de desconto é R${:.2f} .'.format(p-desc))

'''p = float(input('Digite o preço de um produto R$ '))
np = p - (p * 5 / 100)
print('Preço do produto com 5% de desconto é R${:.2f} .'.format(np))'''