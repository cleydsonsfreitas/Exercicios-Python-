from time import sleep

#entrada
nome = str(input("Qual é o seu nome caraiudo?\n"))
print(f"Hoje vamos descobri se um ano é bissexto")

#dados
ano = int(input("Digite um ano\n"))

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

#saida
print("ate a proxima")

sleep(20)