#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
km = float(input('Qual é a distância da sua viagem? '))
print('Você está pretes a começar uma viagem de {:.0f}Km.'.format(km))
if km  <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('E o preço é da sua pasagem será de R${:.2f} '.format(preço))
