#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
import emoji
print (emoji.emojize('🟦'*24))
print(emoji.emojize('         \033[1;36m Analisador de Triângulos 🔼\033[m'))
print (emoji.emojize('🟦'*24))
seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print(emoji.emojize('\033[1;32mOs segmentos acima PODEM FORMAR triângulo ✅\033[m'))
else:
    print(emoji.emojize('\033[1;31mOs segmentos acima NÃO PODEM FORMAR triângulo ❌\033[m'))    