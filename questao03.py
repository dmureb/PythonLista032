'''
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
'''

peso = float(input("Qual é o seu peso em quilos? "))
altura = float(input("Qual é a sua altura em metros? "))

print("Seu peso em gramas é {}".format(peso * 1000))
print("Sua altura em centímetros é {}".format(altura * 100))