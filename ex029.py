'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar
R$7,00 por cada Km acima do limite.
'''
v = float(input('Qual é a velocidade atal do carro? '))
m = (v - 80) * 7.00
if v > 80:
    print('Multado! Você excedue o limite permitido que é de 80Km/h!\nVocê deve pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia! Dirija com segurança!')