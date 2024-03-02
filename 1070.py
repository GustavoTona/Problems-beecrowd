X = int(input())


# começar a inicializar com o 0
num_impares = 0

# Enquanto não encontrarmos os 6 números ímpares consecutivos, continuamos procurando
while num_impares < 6:
    # Se X for ímpar, imprimimos e incrementamos o contador
    if X % 2 != 0:
        print(X)
        num_impares += 1
    # Incrementamos X para verificar o próximo número
    X += 1  