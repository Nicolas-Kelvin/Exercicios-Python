#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1 = str(input('Digite o nome do aluno: '))
a2 = str(input('Digite o nome do aluno: '))
a3 = str(input('Digite o nome do aluno: '))
a4 = str(input('Digite o nome do aluno: '))
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print('{}, parabéns você foi escolhido !'.format(sorteio))