def soma (a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def calculadora():
    n1 = float(input('Digite o primeiro número:'))
    operacao = input("Digite a operação desejada (+, -, *, /): ")
    n2 = float(input('Digite o segundo número:'))
    
    if operacao == '+':
        resultado = soma(n1, n2)
    elif operacao == '-':
        resultado = subtracao(n1, n2)
    elif operacao == '*':
        resultado = multiplicacao(n1, n2)
    elif operacao == '/':
        resultado = divisao(n1, n2)
    else:
        return "Operação inválida!"
    
    print('Resultado:', resultado)
        

while True:
    calculadora()
    continuar = input('Deseja realizar outra operação? (s/n): ')
    if continuar.lower() != 's':
        print("Calculadora encerrada.")
        break