pares = 0

for _ in range(5): # loop para 5 numeros
    valor = int(input())  # lê os numros
    if valor % 2 == 0:  # se o valor 
        pares += 1  # Incrementa a contagem de valores pares

# Imprime a quantidade de valores pares
print(pares, "valores pares")