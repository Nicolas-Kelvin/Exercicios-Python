'''c = 1
while c < 11:
    print(c)
    c = c + 1
print('Fim')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
