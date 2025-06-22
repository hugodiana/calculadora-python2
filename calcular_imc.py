def calcular_imc(peso_param, altura_param):
    imc = peso_param / (altura_param ** 2)
    return imc

peso_do_usuario = float(input("Digite seu peso (em kg):"))
altura_str = float(input("Digite sua altura (em metros):"))

imc_calculado = calcular_imc(peso_do_usuario, altura_str)

if imc_calculado < 18.5:
    classificacao = "Abaixo do peso"
elif imc_calculado >=18.5 and imc_calculado <24.9:
    classificacao = "Peso Normal"
elif imc_calculado >= 25 and imc_calculado <29.9:
    classificacao = "Sobrepeso"
elif imc_calculado >= 30 and imc_calculado <39.9:
    classificacao = "Obesidade"
elif imc_calculado >= 40:
    classificacao = "Obesidade Grave"

print(f"Seu IMC é: {imc_calculado:.2f} e você está: {classificacao}")
