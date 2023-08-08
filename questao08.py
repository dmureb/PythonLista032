'''
Fazer um algorítmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

preço = float(input("Qual o preço de custo do produto? "))
percentual = int(input("Qual o percentual de acrécimo? "))
resultado = preço + (preço * (percentual / 100))

print(f"O valor final da venda, mais o valor de acrécimo é de R${resultado:.2f}")

