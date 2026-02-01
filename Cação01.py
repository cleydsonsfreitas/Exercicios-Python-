from time import sleep 
import sys
import time 

#Entrada
nome = str(input("Qual é o seu nome doador(a)\n"))
print("Vamos saber se você pode doar sangue")
print(f"{nome} para isso vamos precisar saber algumas informações")
print('Vamos lá?')


#colhimento de informações
sexo = str(input("Você é homem ou mulher?\n"))
if sexo == "mulher":
    gravides = str(input("Você está gravida?\n"))
    if  gravides == "sim":
        sys.exit("gravidas não pode doar sangue, finalizamos por aqui")
        
    else:
        print("você é apta a doar vamos lá")

elif sexo == "homem":
    ("vamos continuar")

idade = int(input("Qual é a sua idade?\n"))
print("muito bem")

peso = int(input("Qual é o seu peso?\n"))
print("Estamos quase lá")

#confirmando dados e anaizando 
print(f"Sua idade é {idade}\nSeu sexo é {sexo}\nSeu peso é {peso}\n")

print("Nice vamos analizar seu perfil")
time.sleep(10)

#Função
if peso >= 50 and idade >= 18 and idade < 67:
    print(f"{nome} Parabéns você é o doador perfeito")
    print("Vamos agendar uma doação o mais rápido possivel e salvar vidas!!!")

elif peso >= 50 and idade < 18 and idade> 67:
    print("Você não está apto a doar sangue")

elif peso <= 50 and idade < 18 and idade < 67:
    print("Você não está apto a doar sangue")

elif peso <= 50 and idade > 18 and idade > 67:
    print("Você não está apto a doar sangue")


#Saída
print(f"{nome} Muito obrigado por ter chegado aqui")
print(f"até a proxima campeão")

sleep(20)