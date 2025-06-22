def inverter_lista(minha_lista):
    lista_invertida = []
    for i in range(len(minha_lista) - 1, -1, -1):
        elemento = minha_lista[i]
        lista_invertida.append(elemento)
    return lista_invertida

minha_lista = [1, 2, 3, 4, 5]
inverter_lista = inverter_lista(minha_lista)
print(f"A lista invertida é: {inverter_lista}") 