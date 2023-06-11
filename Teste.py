import numpy

vetor = numpy.empty(10, dtype=numpy.int32)

for posicao in range(0, 10):
    print("Digite o valor", posicao + 1, ": ")
    vetor[posicao] = int(input())

print("Digite o número a ser pesquisado: ")
x = int(input())

for posicao in range(0, 10):
    if vetor[posicao] == x:
        print(x, "foi encontrado na posição ", posicao)