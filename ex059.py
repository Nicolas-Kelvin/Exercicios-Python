'''Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
import emoji
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
sleep(1)
op = 0
while  op != 5:
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input(emoji.emojize('>>>>>👆 Qual é a sua opção? ')))
    sleep(2)
    if op == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
        
    elif op == 2:
        multiplica = n1 * n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, multiplica))
        
    elif op == 3:
        maior = max(n1, n2)
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    
    elif op == 5:
        print('finalizando programa...')
    else:
        print('Opção inválida')
        
    print(emoji.emojize('🟦'*15))
    sleep(2)
    
