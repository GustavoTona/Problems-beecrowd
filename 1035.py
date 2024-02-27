A, B, C, D = map(float, input().split()) # entrada em linha como sempre

def valores(A, B, C, D): #criar uma funcao/def
    
    if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0): # % 2 conferir se é par
        return "Valores aceitos"
    else:
        return "Valores nao aceitos"

print(valores(A, B, C, D))