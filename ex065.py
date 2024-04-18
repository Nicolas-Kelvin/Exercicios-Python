'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n = soma = cont = 0
cond = 'S'

while cond != 'N':
    n = float(input('Digite um número: '))
    soma += n
    cont += 1
    cond = str(input('Quer continuar? [S/N] ')).strip() .upper()
    media = soma / cont
print('Você digitou foi {} números e a média foi {:.2f}'.format(cont, media))
print('O maior valor foi {:.0f} e o menor foi {:.0f}'.format(max(n, n), min(n, n)))

