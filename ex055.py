#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = float('-inf')
menor = float('inf')
for p in range(1,6):
    peso = float(input('Peso da {} pessoa: '.format(p)))
    if peso > maior:
            maior = peso
    if peso < menor:
            menor = peso
print('O menor peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))