'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n = soma = cont = quant = maior = menor = 0
cond = 'S'
while cond != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    quant += 1
    cond = str(input('Quer continuar? [S/N] ')).strip() .upper()
    media = soma / cont
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'Você digitou foi {cont} números e a média foi {media}!')
print(f'O maior valor maior foi {maior} e o menor foi {menor}!')

