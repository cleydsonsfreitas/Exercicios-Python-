from time import sleep
#entrada
nome = input("Qual é o seu nome jovem gafanhoto?")
print(f"Bom telo aqui {nome}. Hoje vamos descobri quantos Dólares você consegue comprar com o que tem na carteira")

#Recolhendo a informação
variavel = int(input("Gafanhoto, quanto dinheiro você tem na carteira?"))

#Conversão
conversão = variavel * 5.46

#Resultado
print(f"Com a quantia de {variavel} você consegue comprar  {conversão} Dolares")
print("Muito obrigado!")
sleep(20)