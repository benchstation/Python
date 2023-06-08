'''
Atividade 1
Receba (input) uma base e uma altura e calcule/mostre a área de um triângulo
# area = (base * altura) / 2
a ) não usando input
b) usando input
'''

# a) não usando input
base = 10
altura = 5
area = (base * altura) / 2
print("A área do triângulo é:", area)

# b) usando input
# Definindo os valores da base e altura obtidos a partir da entrada do usuário
base = float(input("Digite o valor da base do triângulo:\n"))
altura = float(input("Digite o valor da altura do triângulo:\n"))

area = (base * altura) / 2

print(f"A área do triângulo é: {area}")