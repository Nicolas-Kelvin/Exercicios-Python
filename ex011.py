#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabedo que cada litro de tinta, pinta uma área de 2m².
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
área = l * a
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(l, a, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))