numero_teste = int(input()) 
contador = 0

while(contador < numero_teste):
    A, B, C = map(float, input() .split())
    media = (A * 2 + B * 3 + C * 5) / 10 

    print(f"{media:.1f}")
    contador += 1