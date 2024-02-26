#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
tab = int(input('Digite um número: '))
for n in range (0,11):
    print('{} x {:2} = {}'.format(tab, n, tab * n))

    