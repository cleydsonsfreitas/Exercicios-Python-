from time import sleep
import time

#Entrada
nome = str(input("Olá Seja bem vindo, qual é o seu nome?\n"))
print(f"{nome}, prazer em conhece-lo")
sleep(0.5)
print(f"{nome} hoje vamos montar uma lista cadastral para você")
sleep(0.5)

#coletando idade, se tem habilitação e carro
idade = int(input("Qual é a sua idade?\n"))
if idade  >= 18:
    habilitacao = int(input("Você já possui habilitação?\n[1]Sim\n[2]Não\n"))
    if habilitacao == 1:
        print("Importante ter, parabéns, me responda outra coisa\n")
        carro = int(input(f"{nome}, você possui carro?\n[1]Sim\n[2]Não\n"))
        if carro == 1:
            modelo = str(input("Qual é o modelo do seu carro?\n"))
            print(f"{modelo} é um excelente carro")
        else:
            print(f"{nome} Tenho certeza que vai adquirir um em breve\n")
    else:
        print(f"{nome} legal, vai atras de tirar, viu que ficou barato e mais facil? vale a pena\n")
else:
    print(f"{nome} logo mais você faz 18 em")


#dados que temos ate agora
print(f"{nome}, essa é a suatabela até agora")
if idade >= 18 and carro == 1:
    print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
""")

else:
    print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
    """)

#nivel de escolariade
print(f"{nome} agora que pegamos alguns dados sobre você, devemos continuar\n")
sleep(1)
if idade  >= 18:
    escolaridade = int(input("Você já finalizou o ensino médio?\n[1]Sim\n[2]Não\n"))
    if escolaridade == 1:
        print("Bom saber que já finalizou o ensino médio\n")
        faculdade = int(input("Pretende fazer faculdade ou já faz?\n[1]Sim\n[2]Não\n"))
        if faculdade == 1:
            curso = str(input("Qual curso você faz, ou pretende fazer?\n"))
            print(f"Que legal {nome}, acho bastaante interessante o {curso} boa escolha\n")
            faculdade = str(input("Qual é o nome da sua faculade?\n"))
            pp = str(input("Ela é publica ou privada?\n"))
        else:
            print(f"{nome} Certeza? hoje em, dia é importante ter um curso superior")
    else:
        print(f"{nome} logo mais finaliza\n")
else:
    escola = str(input("Pela idade deduzi que ainda está ma escola qual é o nome da sua escola ?\n"))
    ppe = str(input("Elá é publica ou privada?\n"))
    print(f"{nome} essa é uma boa escola\n")

sleep(0.5)
#dados segundo momento
print(f"{nome}, essa é a sua tabela até agora")
if idade >= 18 and carro ==1:
    print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
Já terminou a escola ? = Sim
Curso = {curso}
Faculdade = {faculdade}
Publica ou Privada ? = {pp}

""")
elif idade < 18:
    print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
Já terminou a escola ? = Não
Qual escola estuda? = {escola}
Publica ou Privada ? = {ppe}
""")

# Terceira e ultima parte
print(f"{nome} Você chegou até aqui, muito bem meu consagrado")
print("Agora para finalizar, preciso saber uma coisa")
pais = int(input("Você mora no Brasil?\n[1]Sim\n[2]Não\n"))

if pais == 1:
    estado = int(input(
        """Muito bom ser brasileiro né, de qual estado você é?\n
[01] Acre (AC)
[02] Amapá (AP)
[03] Amazonas (AM)
[04] Pará (PA)
[05] Rondônia (RO)
[06] Roraima (RR)
[07] Tocantins (TO)
[08] Alagoas (AL)
[09] Bahia (BA)
[10] Ceará (CE)
[11] Maranhão (MA)
[12] Paraíba (PB)
[13] Pernambuco (PE)
[14] Piauí (PI)
[15] Rio Grande do Norte (RN)
[16] Sergipe (SE)
[17] Goiás (GO)
[18] Mato Grosso (MT)
[19] Mato Grosso do Sul (MS)
[20] Distrito Federal (DF)
[21] Espírito Santo (ES)
[22] Minas Gerais (MG)
[23] Rio de Janeiro (RJ)
[24] São Paulo (SP)
[25] Paraná (PR)
[26] Rio Grande do Sul (RS)
[27] Santa Catarina (SC)
"""))
    if 1 <= estado <= 7:
        print(f"{nome} Você é da região norte")
        cidaden = str(input("Qual cidade você é ?\n"))
        bairron = str(input("Como chama seu bairro?\n"))
        ruan = str(input("Qual é o nome da sua rua?\n"))
        numerocasan = int(input("Qual é o numero da sua casa?"))

    elif 8 <= estado <= 16:
        print(f"{nome} Você é da região nordeste do pais")
        cidader = str(input("Qual cidade você é ?\n"))
        bairror = str(input("Como chama seu bairro?\n"))
        ruar = str(input("Qual é o nome da sua rua?\n"))
        numerocasar = int(input("Qual é o numero da sua casa?"))

    elif 17 <= estado <= 20:
        print(f"{nome} Você é da região centro - oeste do pais")
        cidadec = str(input("Qual cidade você é ?\n"))
        bairroc = str(input("Como chama seu bairro?\n"))
        ruac = str(input("Qual é o nome da sua rua?\n"))
        numerocasac = int(input("Qual é o numero da sua casa?\n"))

    elif 21 <= estado <= 24:
        print(f"{nome} Você é da região Sudeste do pais")
        cidades = str(input("Qual cidade você é ?\n"))
        bairros = str(input("Como chama seu bairro?\n"))
        ruas = str(input("Qual é o nome da sua rua?\n"))
        numerocasas = int(input("Qual é o numero da sua casa?\n"))

    elif 25 <= estado <= 27:
        print(f"{nome} Você é da região sul do pais")
        cidadel = str(input("Qual cidade você é ?\n"))
        bairrol = str(input("Como chama seu bairro?\n"))
        rual = str(input("Qual é o nome da sua rua?\n"))
        numerocasal = int(input("Qual é o numero da sua casa?\n"))

else:
    paisdefora = str(input("Qual pais você pertecê afinal?\n"))
    cidadee = str(input("Qual cidade você é ?\n"))
    bairroe = str(input("Como chama seu bairro?\n"))
    ruae = str(input("Qual é o nome da sua rua?\n"))
    numerocasae = int(input("Qual é o numero da sua casa?\n"))



#saida
print("chegamos até aqui jovem")
print("após um longo caminho estamos finalizando por aqui")
print("Muito obrigado, até a próxima")
print("Estamos carregando seus dados")

# laço da atividade proposta
for i in range(5, -1, -1):
    print(i)
    time.sleep(1)
print("Seus Dados são:")


if 'modelo' not in locals(): modelo = "Não possui carro"
if 'faculdade' not in locals(): faculdade = "Não cursa"
if 'pp' not in locals(): pp = "Não se aplica"
if 'curso' not in locals(): curso = "Não se aplica"
if 'escola' not in locals(): escola = "Já finalizou"
if 'ppe' not in locals(): ppe = "Não se aplica"




# NORTE
if 1 <= estado <= 7 and pais == 1:
    if idade >= 18 and carro == 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
Já terminou a escola ? = Sim
Curso = {curso}
Faculdade = {faculdade}
Publica ou Privada ? = {pp}
Seu estado é  = {estado}
Sua cidade é = {cidaden}
Seu bairro é = {bairron}
Sua rua é = {ruan}
Numero = {numerocasan}
""")
    elif idade < 18:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
Já terminou a escola ? = Não
Qual escola estuda? = {escola}
Publica ou Privada ? = {ppe}
Seu estado é  = {estado}
Sua cidade é = {cidaden}
Seu bairro é = {bairron}
Sua rua é = {ruan}
Numero = {numerocasan}
""")

    elif idade >= 18 and carro != 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Talvez
Possui carro? = Não
Já terminou a escola ? = Sim
Faculdade = {faculdade} ({pp})
Seu estado é  = {estado}
Sua cidade é = {cidaden}
Seu bairro é = {bairron}
Sua rua é = {ruan}
Numero = {numerocasan}
""")


# NORDESTE
if 8 <= estado <= 16 and pais == 1:
    if idade >= 18 and carro == 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
Já terminou a escola ? = Sim
Curso = {curso}
Faculdade = {faculdade}
Publica ou Privada ? = {pp}
Seu estado é  = {estado}
Sua cidade é = {cidader}
Seu bairro é = {bairror}
Sua rua é = {ruar}
Numero = {numerocasar}
""")
    elif idade < 18:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
Já terminou a escola ? = Não
Qual escola estuda? = {escola}
Publica ou Privada ? = {ppe}
Seu estado é  = {estado}
Sua cidade é = {cidader}
Seu bairro é = {bairror}
Sua rua é = {ruar}
Numero = {numerocasar}
""")
    elif idade >= 18 and carro != 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Talvez
Possui carro? = Não
Faculdade = {faculdade}
Seu estado é  = {estado}
Sua cidade é = {cidader}
""")


# CENTRO - OESTE
if 17 <= estado <= 20 and pais == 1:
    if idade >= 18 and carro == 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
Já terminou a escola ? = Sim
Curso = {curso}
Faculdade = {faculdade}
Publica ou Privada ? = {pp}
Seu estado é  = {estado}
Sua cidade é = {cidadec}
Seu bairro é = {bairroc}
Sua rua é = {ruac}
Numero = {numerocasac}
""")
    elif idade < 18:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
Já terminou a escola ? = Não
Qual escola estuda? = {escola}
Publica ou Privada ? = {ppe}
Seu estado é  = {estado}
Sua cidade é = {cidadec}
Seu bairro é = {bairroc}
Sua rua é = {ruac}
Numero = {numerocasac}
""")
    elif idade >= 18 and carro != 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Talvez
Possui carro? = Não
Faculdade = {faculdade}
Seu estado é  = {estado}
Sua cidade é = {cidadec}
""")


# SUDESTE
if 21 <= estado <= 24 and pais == 1:
    if idade >= 18 and carro == 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
Já terminou a escola ? = Sim
Curso = {curso}
Faculdade = {faculdade}
Publica ou Privada ? = {pp}
Seu estado é  = {estado}
Sua cidade é = {cidades}
Seu bairro é = {bairros}
Sua rua é = {ruas}
Numero = {numerocasas}
""")
    elif idade < 18:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
Já terminou a escola ? = Não
Qual escola estuda? = {escola}
Publica ou Privada ? = {ppe}
Seu estado é  = {estado}
Sua cidade é = {cidades}
Seu bairro é = {bairros}
Sua rua é = {ruas}
Numero = {numerocasas}
""")
    elif idade >= 18 and carro != 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Talvez
Possui carro? = Não
Faculdade = {faculdade}
Seu estado é  = {estado}
Sua cidade é = {cidades}
""")


# SUL
if 25 <= estado <= 27 and pais == 1:
    if idade >= 18 and carro == 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Sim
Possui carro? = Sim
Qual é o modelo = {modelo}
Já terminou a escola ? = Sim
Curso = {curso}
Faculdade = {faculdade}
Publica ou Privada ? = {pp}
Seu estado é  = {estado}
Sua cidade é = {cidadel}
Seu bairro é = {bairrol}
Sua rua é = {rual}
Numero = {numerocasal}
""")
    elif idade < 18:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Não
Possui carro? = Não
Já terminou a escola ? = Não
Qual escola estuda? = {escola}
Publica ou Privada ? = {ppe}
Seu estado é  = {estado}
Sua cidade é = {cidadel}
Seu bairro é = {bairrol}
Sua rua é = {rual}
Numero = {numerocasal}
""")
    elif idade >= 18 and carro != 1:
        print(f"""
Nome = {nome}
Idade = {idade}
Possui Habilitação ? = Talvez
Possui carro? = Não
Faculdade = {faculdade}
Seu estado é  = {estado}
Sua cidade é = {cidadel}
""")


# ESTRANGEIRO
if pais == 2:
    print(f"""
Nome = {nome}
Idade = {idade}
Mora no Brasil? = Não
País = {paisdefora}
Sua cidade é = {cidadee}
Seu bairro é = {bairroe}
Sua rua é = {ruae}
Numero = {numerocasae}
""")





































