peso = float(input("Digite seu peso (em kg):"))
altura = float(input("Digite sua altura (em metros):"))
imc = (peso / (altura ** 2))

if imc < 18.5:
    classificacao = "Abaixo do peso"
if imc >=18.5 and imc <24.9:
    classificacao = "Peso Normal"
if imc >= 25 and imc <29.9:
    classificacao = "Sobrepeso"
if imc >= 30 and imc <39.9:
    classificacao = "Obesidade"
if imc >= 40:
    classificacao = "Obesidade Grave"

print(f"Seu IMC é: {imc:.2f} e você está: {classificacao}")