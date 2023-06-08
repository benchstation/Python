'''
Faça o código necessário para calcular a sequência de
Fibonacci usando FOR e depois faça o mesmo usando função

Exemplo de Saída:
Quantos termos? 7
Sequência de Fibonacci:
0
1
1
2
3
5
8
'''

# LAÇO FOR
termos = int(input("Digite a quantidade de termos para gerar uma sequência Fibonacci: "))

fibonacci = [0, 1]  # Primeiros dois termos da sequência

for i in range(2, termos):
    # fib: novo termo a ser calculado 
    # termo anterior: (índice i - 1) 
    # termo anterior ao anterior: fibonacci[i - 2]
    fib = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(fib)
'''
print("Sequência de Fibonacci:")
for num in fibonacci:
    print(num)
'''
# Acho que fica mais visualmente interessante printar o array logo assim:
print("Sequência de Fibonacci:", fibonacci)

print()

# FUNÇÃO
def fibonacci(termos):
    fibonacci = [0, 1]
    for i in range(2, termos):
        fib = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(fib)
    return fibonacci

termos = int(input("Quantos termos? "))
seq_fibonacci = fibonacci(termos)

print("Sequência de Fibonacci:", seq_fibonacci)
