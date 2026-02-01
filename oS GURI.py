from time import sleep

#Entrada
print("Olá, boa noite! tudo bem gurizada?\n")
print("Hoje sem usar o conceito de lista, vamos inventer os números\n")
nome = str(input("Qual é o seu nome?\n"))
print(f"Boa meu consagrado {nome}")

#coletar dados
print(f"{nome} gurizada, para isso vou precisar de ti\n")
print("Preciso que você digite um número de 4 algoritimo inteiro\n")
print(f"Me ajuda nessa {nome}?\n")

#coletar dados
numeroguri = int(input("digite um número para o pai\n"))


# tem que atribuir
davi = numeroguri

contrario = 0


while numeroguri > 0:

    osdnevida = numeroguri % 10


    contrario = contrario * 10 + osdnevida


    numeroguri = numeroguri // 10



print(f"Por conta do preciosismo do Rodrigo meu caro {nome}, complicou-se o exercicio porém é para o seu número original {davi} o contrario dele é {contrario}\n")

sleep(5)



