positivos = 0 # iniciar com 0 para saber quantos valores positivos 

# Loop para ler seis valores
for _ in range(6):
    valor = float(input())  # Lê um valor
    if valor > 0:  # Verifica se o valor é positivo
        positivos += 1  # Incrementa a contagem de valores positivos
print(positivos, "valores positivos")