def celcius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_para_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

temperatura_digitada = float(input("Digite a temperatura: "))
unidade_original = input("Digite a unidade original (C/F): ").upper()

if unidade_original == 'C':
    temperatura_convertida = celcius_para_fahrenheit(temperatura_digitada)
    print(f"{temperatura_digitada:.2f} Celsius equivalem a {temperatura_convertida:.2f} Fahrenheit. ")
elif unidade_original == 'F':
    temperatura_convertida = fahrenheit_para_celcius(temperatura_digitada)
    print(f"{temperatura_digitada:.2f} Fahrenheit equivalem a {temperatura_convertida:.2f} Celsius. ")
else:
    print("Unidade inválida. Por favor, digite 'C' para Celsius ou 'F' para Fahrenheit.")
    
                                                     