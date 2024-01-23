#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin , cos, tan 
ang = float(input('Digite o ângulo que você deseja: '))
rad = radians(ang)
sen = sin(rad)
cos = cos(rad)
tan = tan(rad)
print('O ângulo de {} tem o SENO de {:.2f}\nO ângulo de {} tem o COSSENO de {:.2f}\nO ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, sen, ang, cos, ang, tan))