# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
import emoji
from time import sleep
computador = randint(0, 5) # Faz o comptador "PENSAR"
print(emoji.emojize('🔸' * 28))
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print(emoji.emojize('🔸' * 28))
jogador = int(input(emoji.emojize('Em que número eu pensei 🤔? '))) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(emoji.emojize('PARABÉNS🥳🎉! Você conseguiu me vencer! ✅'))
else:
    print(emoji.emojize('GANHEI😎! Eu pensei no número {} e não no {}! ❌'.format(computador, jogador)))