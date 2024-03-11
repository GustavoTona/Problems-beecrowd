# Loop for exterior para i variando de 1 a 9, com incremento de 2
for i in range(1, 10, 2):
        # Loop interior para j variando de 7 a 5, com decremento de 1
        for j in range(7, 4, -1):
            # Imprime a string formatada com os valores de i e j
            print("I={} J={}".format(i, j))