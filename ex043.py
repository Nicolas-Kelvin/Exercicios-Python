'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = int(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('Seu IMC: {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.')
elif 18.6 <= imc < 24.9:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 29.9:
    print('Você está com SOBREPESO.')
elif 35 <= imc < 39.9:
    print('Você está com OBESIDADE.')
elif imc > 40:
    print('Você está com OBESIDADE GRAVE.')
    
    