A, B, C = map(float, input().split())

pi = 3.14159

triangulo = A * C / 2
circulo = pi * C ** 2 #area do circulo A = PI . R ao quadrado
trapezio = (A + B) * C / 2 # area do trapezio  A = (a + b).h/2 
quadrado = B * B #certo
retangulo = A * B # certo 


print("TRIANGULO:", format(triangulo, ".3f"))
print("CIRCULO:", format(circulo, ".3f"))
print("TRAPEZIO:", format(trapezio, ".3f"))
print("QUADRADO:", format(quadrado, ".3f"))
print("RETANGULO:", format(retangulo, ".3f"))