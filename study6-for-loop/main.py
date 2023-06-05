### FOR LOOP

quantidade = int(input('Quantidade de notas: '))
media = 0
for i in range (quantidade):
    nota = float(input(f'Qual a nota {i}: '))
    media += nota

media = media/quantidade

print(f'media: {media: .2f}')


####

quantidade = int(input('Quantos numeros? '))

for i in range (quantidade):

    numero = int(input('Qual o numero: '))

    if numero <= 0:

        numero = 1

        print(numero)

    else:

        print(numero)