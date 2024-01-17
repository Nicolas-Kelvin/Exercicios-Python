#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo:')
print ('O tipo primitivo desse valor é ', type(n))
print ('É alfabetico? ', n.isalpha())
print ('É númerico? ', n.isnumeric())
print ('É decimala? ', n.isdecimal())
print ('Só tem espaços? ', n.isspace())
print ('É alpha númerico? ', n.isalnum())
print ('Tem somente letra maiuscula? ', n.isupper())
print ('Tem somente letra minuscula? ', n.islower())


