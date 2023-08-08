'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

valor = float(input("Qual o valor da conta a ser pago no restaurante? "))
print(f"O valor a ser pago, mais os 10% é de R${valor + (valor * 0.10):.2f}")