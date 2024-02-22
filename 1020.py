idade_dia = int(input())

anos = idade_dia // 365 # divisao inteira para calcular quantos anos 
meses = (idade_dia % 365) // 30 # puxando a divisao de cima com o % e depois divindo por 30 que seria um mes

# finalizando com a ultima conta do dia 
dia_restante = idade_dia % 365 # pegando o total dos dias na conta de cima 

# como funciona 
dias = (dia_restante % 30) 

#sobraria 5 dias, já que definimos que o mes tem 30. usamos o % para puxar o restante.

print(f"{anos} anos(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")