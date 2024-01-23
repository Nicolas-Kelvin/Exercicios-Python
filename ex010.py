'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
considere US$1,00 = R$3,27'''
rs = float(input('Digite o valor em R$'))
con = rs / 3.27
print('{}BRL = {:.2f}USD '.format(rs, con))