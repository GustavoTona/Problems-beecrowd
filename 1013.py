a, b, c = map(int, input().split())

# Encontrando o maior entre os dois primeiros valores usando a fórmula
maior_ab = (a + b + abs(a - b)) // 2 #abs retorna apenas o retorna o valor numerico sem o sinal

# Comparando o maior entre os dois primeiros com o terceiro valor
maior = (maior_ab + c + abs(maior_ab - c)) // 2

print(maior, "eh o maior")