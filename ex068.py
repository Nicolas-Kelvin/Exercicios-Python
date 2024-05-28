'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from time import sleep
from random import randint
comp = randint(0,11)
p = 'P'
i = 'I'
cont = 0
print('=-' * 12)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 12)
sleep(1)
while True:
  
  jogador = int(input('Digite um valor: '))
  cond = str(input('Par ou Ímpar? [P/I]')).strip().upper()
  if jogador > 0:
      if (jogador + comp)  % 2 == 0:
          print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {jogador + comp} deu PAR')
          if cond == p:
              cont += 1
              print('Você VENCEU!')
              sleep(1)
              print('Vamos jogar novamente.....')
          else:
              print('Você PERDEU!')
              print(f'GAME OVER! Você venceu {cont}')
              break    
         
      elif (jogador + comp) % 2 != 0:  
          print(f'Você jogou {jogador} e o computador jogou {comp}. Total de {jogador + comp} deu ÍMPAR')
          if cond == i:
              cont += 1
              print('Você VENCEU!')
              sleep(1)
              print('Vamos jogar novamente.....')
          else:
              print('Você PERDEU!')
              print(f'GAME OVER! Você venceu {cont}')
              break
  else:
    print('Você digitou numeros negativos que são considerados inválidos!')
    break

'''
Correção do exercicio:

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] '))
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}',  end='')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente....')
print(f'GAME OVER! Você venceu {v} vezes.')'''
      
  

