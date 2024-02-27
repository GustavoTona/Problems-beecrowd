valor = float(input())

# Convertendo o valor para centavos para facilitar os cálculos
valor_centavos = int(valor * 100)

# Lista das notas que estão pedindo
notas = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

# Imprimindo o valor lido
print("NOTAS:")

# Iterando sobre as notas para contar quantas são necessárias
for nota in notas:
    qtd_notas = valor_centavos // nota
    if nota >= 100:
        print(f"{qtd_notas} nota(s) de R$ {nota/100:.2f}")

# Agora imprimindo as moedas
print("MOEDAS:")

# Iterando novamente, agora para as moedas
for nota in notas: 
    qtd_notas = valor_centavos // nota
    if nota < 100:
        print(f"{qtd_notas} moeda(s) de R$ {nota/100:.2f}")
    valor_centavos -= qtd_notas * nota