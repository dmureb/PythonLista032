'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

anos = int(input("Quantos anos você tem? "))
meses = int(input("Quantos meses se passou desde seu ultimo aniversário? "))
dias = int(input("Quantos dias se passou neste último mês? "))
resultado = (anos * 365) + (meses * 30) + dias

print(f"Sua idade em dias é correspondente a: {resultado}")