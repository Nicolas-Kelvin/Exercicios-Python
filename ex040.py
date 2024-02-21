''' Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(n1, n2, média))
if média >= 7.0:
    print('O aluno está APROVADO.')
elif 7 > média >= 5 :
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5 :
    print('O aluno está REPROVADO')

         