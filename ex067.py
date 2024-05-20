'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.'''

while True:
    print('-'* 34)
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-'* 34)
    if n > 0:
        for tab in range(1, 11):
            s = tab * n
            print(f'{n} x {tab:2} = {s}')
    else:
        break
print('PROGRAMA TABUADA ENCERRADO.\nVolte sempre!')