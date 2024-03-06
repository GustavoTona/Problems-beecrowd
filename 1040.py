# Leitura das quatro notas
N1, N2, N3, N4 = map(float, input().split())

# Cálculo da média com pesos
media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

# Imprimindo a média
print("Media: {:.1f}".format(media))

# Verificando a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    # Leitura da nota do exame
    nota_exame = float(input())
    print("Nota do exame: {:.1f}".format(nota_exame))
    # Recálculo da média com o exame
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    # Imprimindo a média final
    print("Media final: {:.1f}".format(media_final))