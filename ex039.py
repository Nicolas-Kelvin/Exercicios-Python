#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import emoji
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
falta = 18 - idade
alistamento = falta + atual

if idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.\nVocê tem que se alistar IMEDIATAMENTE.'.format(nasc, idade, atual))
elif idade < 18:
    print(emoji.emojize('Quem nasceu em {} tem {} anos em {}.\nAinda falta {} anos para o alistamento\nSeu alistamento será em {} 📋.'.format(nasc, idade, atual, falta, alistamento)))
elif idade > 18:
    saldo = idade - 18
    print('quem nasceu em {} tem {} anos em {}.\nVocê  já deveria ter se alistado há {} anos.'.format(nasc, idade, atual, saldo))
    ano = atual - saldo
    print('Seu alistamneto foi em {}'.format(ano))   
    