from time import sleep
#entrada
nome = input("Olá estudante, qual é o seu nome?\n")
print(f"É bom ter você aqui {nome}\n")
print("Hoje vamos fazer algumas converções")

#recepção de dados
valor_em_metros = int(input("Digite qualquer número em metros\n"))

#conversões
quilometros = valor_em_metros / 1000
hectometros = valor_em_metros / 100
decametros = valor_em_metros / 10
decimetros = valor_em_metros * 10
centimetros = valor_em_metros * 100
milimetros = valor_em_metros * 1000

#resultados
print(f" Parábens seu número de metros para Quilômetros é:{quilometros}\n")
print(f" Parábens seu número de metros para Hectômetros é{hectometros}\n:")
print(f" Parábens seu número de metros para Decâmetros é{decametros}\n:")
print(f" Parábens seu número de metros para Decímetros é{decimetros}\n:")
print(f" Parábens seu número de metros para Centímetros é{centimetros}\n:")
print(f" Parábens seu número de metros para Milímetros é:{milimetros}\n")
print("Muito obrigado!")
sleep(20)