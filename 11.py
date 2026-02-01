from time import sleep
#conversando com o usuario
nome = input("Hellol young, How are you? I hope you are well!! What is your name?\n ")

print("Hoje vamos descobri se você foi um bom aluno esse semestre em Lógica da programação e calcularemos sua Média")
print("Sua média é nota01 + nota02 e a media é igual a 5 se der mais você passou, se der menos nos vemos semestre que vem")

#informações
nota01 = int(input("Me conte qual foi a sua primeira nota\n"))
nota02 = int(input("Me conte qual foi a sua segunda  nota\n"))

#calculando média
media = (nota01 + nota02) / 2

#Ver o que acontece
if media >= 5:
    print(f"Parabéns sua média foi {media:.2f} você conseguiu, não nos veremos semeste que vem")
else:
    print(f"Sua média foi {media:.2f} nos vemos semestre que vem ")

print("Muito obrigado")

sleep(20)