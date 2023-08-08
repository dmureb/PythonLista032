'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura²
Obs: peso em quilos e altura em metros.
'''
import math

peso = float(input("Qual é o seu peso em quilos? "))
altura = float(input("Qual é a sua altura em metros? "))

print(f"Seu valor do índice de massa corporal é de {peso / (math.pow(altura,2))}")