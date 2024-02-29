pares = 0
impar = 0
positivos = 0
negativos = 0

for _ in range(5): # loop para 5 numeros
    valor = int(input())  # lê os numros
    if valor % 2 == 0:  # se o valor 
        pares += 1  # Incrementa a contagem de valores pares

    else:  # o resto eu coloco como impar 
        impar += 1  # Incrementa a contagem de valores impar

    if valor > 0:  # Verifica se o valor é maior que zero
        positivos += 1  # Incrementa a contagem de valores positivos

    if valor < 0:  # se o valor é menor que zero 
        negativos += 1  # Incrementa a contagem de valores negativo

# Imprime a quantidade de valores pares
print(pares, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")

