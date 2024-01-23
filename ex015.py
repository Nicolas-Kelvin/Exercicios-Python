'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''
km = float(input('Digite a quantidade percorrida em KM '))
d = int(input('Digite a quantidade de dias alugado: '))
total = (km * 0.15) + (d * 60.00)
print('O custo do  carro alugado é de R${:.2f}R$.'.format(total))