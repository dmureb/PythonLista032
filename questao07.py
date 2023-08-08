'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

valor = float(input("Qual o valor da sua compra? "))
prestacoes = int(input("Quantas prestações foram escolhidas? "))
resultado = valor / prestacoes

print(f"O valor a ser pago em cada prestação é de R${resultado:.2f}")