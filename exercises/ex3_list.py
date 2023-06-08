# Desenvolva o programa que leia vários(N) números digitados e mostre estas informações: 
# A) Quantidade de elementos dados ;
# B) Soma dos valores ;
# C) media dos valores ;
# D) porcentagem(ate duas casas decimais ) de números pares ;
# (( Pode usar o comando While ou For ))

lista = []
while True:
    n = int(input('Digite um número (ou cancele com -1): '))
    if n >= 0:
        # Adicionam-se elementos à lista
        lista.append(n)
    else:
        # Lista continua vazia
        break
if not lista: # Listas vazias retornam False :o
    print('Nenhum número foi digitado.')
else: # Apenas se a lista não estiver vazia esse código roda
    numerosPares = 0
    for n in lista:
        if n % 2 == 0:
            numerosPares += 1

    print(f'Foram digitados {len(lista)} números')
    print(f'A soma dos números é: {sum(lista)}')
    print(f'A porcentagem de números pares é: {(numerosPares/len(lista))*100: .2f}%')