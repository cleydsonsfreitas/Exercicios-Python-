from time import sleep
#saudação
nome = input("Sei que não aguenta mais dizer seu nome, porém preciso saber ele kkkkkkkk Qual é?")
print(f"Prometo que por hoje é a ultima vez que pergunto seu nome {nome} agora só segunda kkkkkkkkkkk")
print("Agora vamos descobrir a área da sua parede e saber qaunto de tinta eu preciso para pintar ela")
print(f"Para isso vou precisar de algumas informações,Vamos lá {nome}")

#Pegando informações
altura = int(input("Qual é a altura da sua parede?"))
largura = int(input("Qual é a largura da sua parede?"))

#Área
area = altura * largura
print(f"Muito bem, a área da sua parede é: {area}\n")

#Tinta necessária
print("Vamos descobrir quanto de tinta será necessário")
print("Sab-se que 1 Litro pinta 2m^2")
tinta= int(input("Digite a área da sua parede calculada anteriormente"))

resultado = (tinta /2 )*1
print(f"Será necessário {resultado} litros de tinta para pintar a sua parede!")
print("Muito obrigado!")
sleep(20)




