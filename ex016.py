#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um número: '))
print('O número {} tem a porção Inteira é {}'.format(num, trunc(num)))