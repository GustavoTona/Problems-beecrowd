import math #importar a biblioteca math

x_1, y_1 = map(float, input().split())
x_2, y_2 = map(float, input().split())

#usar o math.sqrt é calcular essa raiz garatindo o resultado correto (calcular dois pontos do plano cartesiano)
distancia = math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2) 

print(format(distancia, '.4f'))

