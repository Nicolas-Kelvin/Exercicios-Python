''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


print('-' * 25)
print('CADASTRE UMA PESSOA')
print('-' * 25)
tot18 = totH =  totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF' :
        sexo = str(input('Sexo: [M/F] ')).strip().upper() [0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    cond = ' '
    while cond not in 'SN':
        cond = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if cond == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao total temos {totH} homens cadastrados')
print(f'E temos {totM20} mulheres com menos de 20 anos')
        
    