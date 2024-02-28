tabela = {
    1 : 4.00,
    2 : 4.50,
    3 : 5.00, 
    4 : 2.00,
    5 : 1.50,
}

produto, quantidade = map(int, input().split())

produto_selecionado = tabela[produto]

total = produto_selecionado * quantidade

print("Total: R$ {:.2f}".format(total))

