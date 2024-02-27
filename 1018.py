valor = int(input())

# Lista das notas disponíveis em ordem decrescente
notas = [100, 50, 20, 10, 5, 2, 1]

print(valor)

for nota in notas:
    qtd_notas = valor // nota 
    print(f"{qtd_notas} nota(s) de R$ {nota},00")
    valor -= qtd_notas * nota