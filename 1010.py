pecas_1, quantidade_1, valor_1 = map(float, input().split())
pecas_2, quantidade_2, valor_2 = map(float, input().split())

total = (quantidade_1 * valor_1) + (quantidade_2 * valor_2)

print("VALOR A PAGAR: R$", format(total, ".2f"))