''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''


print('-' * 25)
print('CADASTRE UMA PESSOA')
print('-' * 25)
while True:
    m = 'Mm'
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    cond = str(input('Quer continuar? [S/N] ')).strip().upper()
        
    