from time import sleep

#Entrada
nome = str(input("Menzinho quais eres tu nombre?\n"))
print("Hoje vamos descobri se os tamanhos das restas escolhidos por você pode formar um triangulo")

#Dados
reta1 = int(input("Digite o lado 1\n"))
reta2 = int(input("Digite o lado 2\n"))
reta3 = int(input("Digite o lado 3\n"))

#Equação
if reta1 + reta2 > reta3:
    print("Parabens você pode formar um triangulo")
else:
    print("Porra mano, tu não pode formar um triangulo")

#Saída
print("Thal bobo")
sleep(20)
