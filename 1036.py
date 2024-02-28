import math

A, B, C, = map(float, input().split())

delta = (B ** 2) - 4 * A * C 


# A na equação quadrática é igual a zero, o que faz com que a equação perca a forma quadrática. E o cálculo das raízes não é possível usando a fórmula quadrática.
if delta <= 0 or A == 0: # verificar o delta já que o delta nao pode ser 0.
    print("Impossivel calcular")

else: 
    x_1 = (- B + math.sqrt(delta)) / (2 * A)  # Raiz quadrada de delta "square root", por isso o "sqrt".
    x_2 = (- B - math.sqrt(delta)) / (2 * A)

    print("R1 =", format(x_1, ".5f"))
    print("R2 =", format(x_2, ".5f"))