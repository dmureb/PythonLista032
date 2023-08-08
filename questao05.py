'''
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
'''

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

soma = num1 + num2
sub = num1 - num2
sub2 = num2 - num1
mult = num1 * num2
div = num1 / num2
resto = num1 % num2

print(f"Soma: {soma}")
print(f"Subtração do primeiro pelo segundo: {sub}")
print(f"Subtração do segundo pelo primeiro: {sub2}")
print(f"Multiplicação: {mult}")
print(f"Divisão: {div}")
print(f"Resto da divisão: {resto}")