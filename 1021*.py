# Ler o valor monetário fornecido
valor = float(input())

# Definir as notas e moedas disponíveis
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Inicializar as variáveis para contar a quantidade de cada nota e moeda
quantidade_notas = []
quantidade_moedas = []

# Calcular a quantidade de cada nota necessária
for nota in notas:
    quantidade = int(valor // nota)
    quantidade_notas.append(quantidade)
    valor -= quantidade * nota

# Calcular a quantidade de cada moeda necessária
for moeda in moedas:
    quantidade = int(valor // moeda)
    quantidade_moedas.append(quantidade)
    valor -= quantidade * moeda

# Imprimir a quantidade de cada nota
print("NOTAS:")
for i in range(len(notas)):
    print(f"{quantidade_notas[i]} nota(s) de R$ {notas[i]:.2f}")

# Imprimir a quantidade de cada moeda
print("MOEDAS:")
for i in range(len(moedas)):
    print(f"{quantidade_moedas[i]} moeda(s) de R$ {moedas[i]:.2f}")