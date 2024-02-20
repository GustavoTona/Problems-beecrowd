nome_vendedor = input()

# Lendo o salário fixo do vendedor e o total de vendas efetuadas
salario_fixo = float(input())
total_vendas = float(input())

# Calculando a comissão (15% das vendas)
comissao = total_vendas * 0.15

# Calculando o total a receber
total_receber = salario_fixo + comissao

# Imprimindo o resultado formatado com duas casas decimais
print(f"TOTAL = R$ {total_receber:.2f}")