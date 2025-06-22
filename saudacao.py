# 1. Pede o nome do usuário e guarda em uma variável
nome = input("Qual é o Seu Nome? ")
# 3. Pede de onde a pessoa exibe uma mensagem de boas-vindas
cep = input("De onde você é?")
# 2. Exibe uma mensagem de boas-vindas personalizada
print(f"Olá, {nome}! Seja bem-vindo(a) ao mundo Python! Vi aqui que você é de {cep} correto?")
# 4 Espera o usiario responder sim ou não
resposta = input("Você está certo(a)? (sim/não) ")
# 5. Se a resposta for sim, exibe uma mensagem de que não está longe
if resposta.lower() == "sim":
    resposta = "sim"
elif resposta.lower() == "não":
    resposta = "não"
# 6. Se a resposta for não, exibe uma mensagem de que não tem problema
if resposta.lower() == "sim":
    resposta = "sim"
elif resposta.lower() == "não":
    resposta = "não"

if resposta.lower() == "sim":
    resposta = "sim"
    
if {resposta} == "sim":
    print("Nossa, que legal! Aparentemente você não está longe de mim!")
if resposta == "não":
    print("Poxa, que pena! Mas não tem problema, o importante é que você está aqui!")
