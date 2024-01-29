#Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando sue nome...')
print('Seu nome com letra maiúscula é {}'.format(nome.upper()))
print('Seu nome com letra minúscula é {}'.format(nome.lower()))
print('Seu nome tem todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro nome tem {} letras'.format(nome.find(' ')))
'''nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando sue nome...')
print('Seu nome com letra maiúscula é', nome.upper())
print('Seu nome com letra minúscula é', nome.lower())
print('Seu nome tem ao todo', len(nome) - nome.count(' '),'letras')
print('Seu primeiro nome é', nome.split()[0], 'e ele tem', len(nome.split()[0]),'letras')'''