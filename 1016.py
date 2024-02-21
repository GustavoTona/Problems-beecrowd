'''

Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.

Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.

Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

Entrada
O arquivo de entrada contém um número inteiro.

Saída
Imprima o tempo necessário seguido da mensagem "minutos".


'''

distancia = int(input())

# Velocidade relativa entre os carros (carro Y alcançando o carro X)
velocidade_relativa = 90 - 60  # 90 km/h (carro Y) - 60 km/h (carro X)

# Tempo necessário para o carro Y alcançar o carro X (em horas)
tempo_horas = distancia / velocidade_relativa

# Convertendo o tempo de horas para minutos
tempo_minutos = tempo_horas * 60

# Imprimindo o resultado
print(round(tempo_minutos), "minutos") #round para arredondar para o proximo numero inteiro