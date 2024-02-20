numero_funcionario = int(input())
horas_trabalhadas = int(input())
valor_por_hora = float(input())

# Calculando o salário do funcionário
salario = horas_trabalhadas * valor_por_hora

# Imprimindo o número e o salário do funcionário formatado com duas casas decimais
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = $ {salario:.2f}")