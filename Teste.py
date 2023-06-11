contador1 = 1
positivo = 0
negativo = 0
numero = 0

while contador1 <= 5:
    print("Informe um número")
    numero = int(input())

    if numero > 0:
        positivo +=1
    if numero < 0:
        negativo += 1

    contador1 += 1
print("Total de número positivo é ", positivo)
print("Total de número negativos é ", negativo)