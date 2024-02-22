n = int(input())

horas = n // 3600 # // é o operador de divisão inteira sem casas decimais, nao precisa colocar round no print
minutos = (n % 3600) // 60 #  usamos % para calcular o restante da conta que seria os segundos
segundos = n % 60 # calcula os segundos restante com o % 

print(f"{horas}:{minutos}:{segundos}") #aprendi um novo jeito de printar as coisas 