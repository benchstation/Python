# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada. 

# A) Faça uma tabuada usando FOR dentro de um WHILE.
# B) Faça um código, usando FOR, que mostre todas as tabuadas(1 até 10).

import time
print("Bem-vindo ao Gerador de Tabuada!")
time.sleep(2)
print("Você pode digitar um número entre 1-10 para gerar sua respectiva tabuada.")
time.sleep(3)

# A) Gerando tabuada baseada em input do usuário incluindo também FOR dentro de um WHILE
flag = 0
flag2 = False
while True:
    if flag == 0:
        msg = "Digite um número para ver a tabuada (ou -1 para cancelar): "
    elif flag == 1:
        msg = "Clique ENTER (ou -1 para cancelar): "
    numero = int(input(msg))
    
    if numero == -1:
        break
    
    while numero < 1 or numero > 10:
        numero = int(input("Digite um número entre 1 e 10: "))
    
    print(f"Tabuada do número {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
    print()  # Adiciona uma linha em branco entre as tabuadas
    flag = 1
    if flag == 1 and not flag2:
        time.sleep(1)
        print("Massa! Você já testou a funcionalidade :)")
        time.sleep(2)
        print("Mas ela nem é tão incrível assim, sabia? :/")
        time.sleep(2)
        print("Ao clicar ENTER (mesmo que sem querer), o Python vai crashar o programa.")
        time.sleep(2)
        print("Isso porque um ValueError vai acontecer ao tentar converter uma string vazia em um número.")
        time.sleep(3)
        print("Mas eu tenho a solução!")
        time.sleep(2)
        print("Se estiver curiose, descomente o código aqui em baixo..!")
        time.sleep(3)
        print("Mas antes, só para encerrar a brincadeira,")
        time.sleep(2)
        print("Tente clicar ENTER para ver o que acontece...")
        time.sleep(2)
        flag = 2
        flag2 = True
    if not flag == 2 and flag2:
        time.sleep(1)
        print("Tente clicar ENTER para ver o que acontece...")
        time.sleep(2)

    
print("Programa encerrado. Obrigado!")

time.sleep(2)
print("Agora, eu te convido a descomentar o código abaixo e tentar diferentes tipos de input.")
time.sleep(3)
print("Pode ser um número entre 1-10, um número real, um palavra, um caractere especial...")
time.sleep(3)
print("Ou a bendita string vazia..! (Basta dar um ENTER)")
time.sleep(3)
print("Dessa vez vai dar certo. Juro.")
time.sleep(2)
print()
time.sleep(2)
print("(... Ok. Só não dá certo se você clicar Ctrl + C.)")
time.sleep(3)

print()

'''
print()
print()

### Versão extendida pra resolver o bug da string vazia ('')
def validando_e_convertendo_input(_str, _str_erro):
    while True:
        # Recebendo o input passado na função
        user_input = input(_str)
        # Checando por uma string vazia e printando uma msg personalizada
        if user_input == "" and not user_input == "-1":
            print("O valor fornecido é vazio. Por favor, tente novamente.")
            continue 
        # Aproveitando pra checar se o input inclui só números (e se não é a condição de saída)
        if not user_input.isdigit() and not user_input == "-1": # (Python tem tudo que se imagina msmo, q dlç)
            print(_str_erro)
            continue
        
        valor = int(user_input)
        return valor # return sai da função o que quebra também o laço

print("Bem-vindo ao Gerador de Tabuada 2.0!")
print("Digite -1 a qualquer momento para sair.")
programa_encerrado = False # flag

while not programa_encerrado:
    numero = validando_e_convertendo_input("Digite um número para ver a tabuada: ", "Entrada inválida. Digite um número válido.")
    
    if numero == -1:
        programa_encerrado = True
        continue # skippa e recomeça com a flag dessa vez verdadeira pra quebrar o while

    print(programa_encerrado)
    while numero < 1 or numero > 10:
        numero = validando_e_convertendo_input("Digite um número entre 1 e 10: ", "Entrada inválida. Digite um número válido entre 1 e 10.")

    print(f"Tabuada do número {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

    print()

print("Programa encerrado. Obrigado!")
exit()
'''

'''
Daí você deve estar se perguntando. Por que eu fiz esse negócio todo?
        A verdade é que eu não achei que seria tão complicado assim :''D
                Mas valeu o desafio
'''

time.sleep(10)

# B) Tabuada auto-gerada (1-10)
for numero in range(1, 11):
    print(f"Tabuada do número {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print()
print("Essa é a tabuada completa auto-gerada usando laço FOR.")