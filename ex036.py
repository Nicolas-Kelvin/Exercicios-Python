#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual o seu salario? R$'))
anos = int(input('Quantos anos de financiamento? '))
exedente = 30 / 100 * salario
prestação = casa / (anos * 12)
if exedente >= prestação:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo pode ser CONCEDIDO! '.format(casa, anos,prestação ))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo pode ser NEGADO!'.format(casa, anos, prestação))

    