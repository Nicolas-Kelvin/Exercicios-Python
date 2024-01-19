#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int(input('Digite um número: '))

print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.'.format(n, (n*2), n, (n*3), n, (math.sqrt(n))))

#n = int(input('Digite um número: '))
#dob = n * 2
#tri = n * 3
#rai = math.sqrt(n) 
#print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz quadrada de {} é {:.2f}.'.format(n, dob, n, tri, n, rai))