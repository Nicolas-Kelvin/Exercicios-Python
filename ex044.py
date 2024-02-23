'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''
print('{:=^40}'.format(' LOJAS KELVIN '))
compra = float(input('Preço das compras: R$'))
dinheiro = compra - (compra * 10) / 100 
cartão = compra - (compra * 5) / 100
x2 = compra / 2
juros = compra + (compra * 20) / 100 
  
print('''FORMAS DE PAGAMENTO
      [ 1 ] à vista dinheiro/cheque
      [ 2 ] à vista cartão
      [ 3 ] 2x no cartão
      [ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(compra, dinheiro))
elif opção == 2:
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(compra, cartão))
elif opção == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(x2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    vparcelas = juros / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, vparcelas))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(compra, juros))      
else:
    total = 0
    print('OPÇAO INVÁLIDA de pagamento. tente novamente!')

    