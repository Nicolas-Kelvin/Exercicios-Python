#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
f = (input('Digite nome funcionário: '))
s = float(input('Digite o salário atual R$ '))
aum = s + (s * 15 / 100)
print('O salário de {} com 15% de aumento passa a ser R${:.2f}'.format(f, aum))


