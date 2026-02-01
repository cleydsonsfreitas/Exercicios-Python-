from time import sleep

#Entrada
nome = str(input("Menzinho quais eres tu nombre?\n"))
print("Hoje vamos descobri se os tamanhos das restas escolhidos por você pode formar um triangulo")

#Dados
reta1 = int(input("Digite o lado 1\n"))
reta2 = int(input("Digite o lado 2\n"))
reta3 = int(input("Digite o lado 3\n"))


#Conta
formação_triangulo = reta1 + reta2 > reta3

#Equação
if formação_triangulo and reta1 == reta2 and reta2 == reta3:
    print("Porra mano, tu pode formar um triangulo e ele é equilatero")

elif formação_triangulo and reta1 == reta2 and reta3 != reta1 and reta3 != reta2:
    print("Porra mano, tu  pode formar um triangulo e ele é isóceles")

elif formação_triangulo and reta1 != reta2 and reta2 != reta3:
    print("Porra mano, tu  pode formar um triangulo e ele é escaleno")

elif reta1 + reta2 < reta3:
    print("Porra mano, tu  não pode formar um triangulo ")


#Saída
print("Thal bobo")
sleep(20)
