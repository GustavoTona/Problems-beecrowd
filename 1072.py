
N = int(input())

dentro = 0 # iniciar com 0 para saber quantos valores positivos 
fora = 0 

# Loop para ler seis valores
for _ in range(N):

    num = int(input())  # Lê um valor
    if 10 <= num <= 20:  # 10 <= X: o valor de X é maior ou igual a 10. X <= 20: o valor de X é menor ou igual a 20
        dentro += 1  # Incrementa a contagem de valores positivos
    else:
        fora +=1

print(dentro, "in")
print(fora, "out")