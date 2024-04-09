''' Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from time import sleep
from random import randint
computador = randint(0, 10)#Faz computador "PENSAR"
print('Sou seu computador...')
sleep(2)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(2)
print('Será que você consegue adivinhar qual foi?')
sleep(2)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print("Acertou com {} tentativas, Parabéns!".format(palpites))

