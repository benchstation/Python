'''
Atividade 2
Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse intervalo), 
depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno passou ou não. 

A escola aceita notas 7 (sete) acima para aprovação.

Atenção para a indentação do código (inclusive na entrega dos exercícios)

n1 = int(input(“Nota-1: “))
if n1 < 0 or n1 > 10:
   # inválido
else:
    n2 …
    if n2 < 0 or n2 > 10:
         print (“Inválido”)
    else:
          n3 …
'''
print("Nessa escola hipotética, aqueles que possuem uma média final igual ou maior que 7 serão aprovados.")
print("Você será solicitado a inserir três notas para verificar se você passou ou não.")

media = 0

n1 = float(input("Informe sua primeira nota (0-10): "))
if n1 < 0 or n1 > 10:
    print("Sua 1ª nota ((%.1f)) é inválida!"% (n1))
    exit()

n2 = float(input("Informe sua segunda nota (0-10): "))
if n2 < 0 or n2 > 10 :
    print("Sua 2ª nota ((%.1f)) é inválida!"% (n2))
    exit()

n3 = float(input("Informe sua terceira nota (0-10): "))
if n3 < 0 or n3 > 10:
    print("Sua 3ª nota ((%.1f)) é inválida!\n"%(n3))
    exit()

media = n1 + n2 + n3
media /= 3

if media >= 7 and media <= 10 :
    print("\nVocê foi aprovado com média: ((%.2f)), parabéns." % (media))

elif media < 0 or media > 10 :
    print("\nOs valores informados são inválidos, por favor, tente novamente.")
else:
    print("\nVocê foi reprovado com média: ((%.3f)), tente novamente no próximo semestre."%(media))
