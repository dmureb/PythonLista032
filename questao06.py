'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês
'''

nome = input("Qual é o seu nome, vendedor? ")
salario = float(input("Qual é o seu salário fixo? "))
vendas = float(input("Qual o total de vendas em dinheiro? "))

print("Seu nome: {}".format(nome))
print("Seu salário fixo: {}".format(salario))
print("Sua comissão: {}".format(vendas * 0.15))
print(f"Seu salário final: R${salario + (vendas * 0.15):.2f}")