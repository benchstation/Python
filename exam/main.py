### AVALIAÇÃO MINICURSO PYTHON

# (1)
# Escreva um programa que repita a leitura de uma senha até que ela seja válida. 
# Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". 
# Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. 
# Considere que a senha correta é o valor 2002. 

tentativa = True
senha = input("Digite a senha:\n")
senha_correta = "2002"
while (tentativa):
    if (senha != senha_correta) :
        print("Senha Inválida")
        senha = input("Digite a senha:\n")
    else:
        tentativa = False
        print("Acesso Permitido")


# (2)
# Considere o seguinte código:
# Qual será o resultado da variável "total"?

count = 0
total = 0

while count < 5:
    total += count 
    count += 1
    if count == 3:
        continue
    # print(count)
    total += count
    # print(total) # 22

# (3)
# Qual das seguintes opções descreve corretamente o conceito de "indentação" em Python?
# (a) É um tipo de estrutura de controle que permite repetir um bloco de código.
# (b) É um operador utilizado para realizar operações aritméticas
# >(c) É a forma como os espaços em branco são usados para definir a estrutura de um bloco de código.
# (d) É um método para converter um tipo de dado em outro tipo em Python.

# (4)
# Crie um programa que imprime de 0 ate 12 e fazendo pulos de três(3).
# (use o comando For)

for n in range(0, 13, 3):
    print(n)


# (5) 
# Nome completo

# (6) 
# Desenvolva o programa que leia vários(N) números digitados e mostre estas informações: 
# A) Quantidade de elementos dados ;
# B) Soma dos valores ;
# C) media dos valores ;
# D) porcentagem(ate duas casas decimais ) de números pares ;
# (( Pode usar o comando While ou For ))

lista = []
entrada = input("Digite um número positivo (ou um negativo para interromper o programa):\n")
n = int(entrada)
while (n >= 0):
    lista.append(n)
    entrada = input("Digite um número positivo (ou um negativo para interromper o programa):\n")
    n = int(entrada)
print(lista)
print("Quantidade de valores dados:", len(lista))
print("Soma dos valores dados:", sum(lista))
media_lista = sum(lista) / len(lista)
print("Media dos valores dados:", media_lista)
# Porcentagem de números pares
par = 0
for n in range(len(lista)):
    if lista[n] % 2 == 0:
        par += 1
    print("Valor na lista:", lista[n])
    print("Números pares:", par)

porcentagem = (par / len(lista)) * 100
print(f"Porcentagem de números pares: {porcentagem: .2f}%")


# (7)
# Faça um programa que recebe um //nome (str) e imprime
# (seja bem vindo a Python //nome) 

nome = input("Digite um nome: ")
print(f"Seja bem vindo a Python, {nome}!")


# (8)
# Criar um lista com 5 números diferentes 
# A ) Acrescente o valor 3 e 4 na lista 
# B ) Faça com que eles virem uma lista decrescente 
# C ) Depois mostre o tamanho da lista 
# D ) Apaga a primeira posição da lista e coloca o valor 35
# E ) Imprimir a lista

array = [2, 3, 28, 11, 8]
print(array)
array.append(3)
array.append(4)
print(array)
array.reverse()
print(array)
tamanho = len(array)
print("Tamanho da lista:", tamanho)
del array[1]
array.insert(1, 35)
print(array)


# (9)
# Def permite um tipo de programação, dentre as opções abaixo, qual é verdadeira?
# (a) Programação Orientada a Objeto
# >(b) Programação Estruturada
# (c) Programação Por Def
# (d) Programação Orientada a Função

# (10)
# Qual das seguintes opções descreve corretamente o conceito de "variável" em Python?
# >(a) Uma variável é um nome associado a um valor ou objeto na memória, que pode ser utilizado para armazenar e manipular dados.
# (b) Uma variável é uma função que executa um conjunto específico de instruções.
# (c) Uma variável é uma estrutura de dados que armazena informações em formato de tabela.
# (d) Uma variável é um objeto que permite a interação com o usuário através de uma interface gráfica.

# (11)
# Crie um programa que receba um valor e se esse valor for inferior a um salário mínimo (R$ 1.200,00) 
# informe que o salário está fora da legislação e se for negativo ou zero informe 
# que o salário está invalido (usa if e se for necessário pode usar elif e else ). 
salario = float(input("Digite o salário:(XXXX.XX)\n"))
if salario > 0 and salario < 1200.00:
    print("O salário está fora da legislação. Esse patrão é um explorador.")
elif salario <= 0:
    print("Salário inválido. Digite um valor de salário válido.")
else:
    print("O salário está de acordo com a legislação.")


