def calcular_media(lista_de_notas):
    if len(lista_de_notas) == 0:
        return 0.0
    
    soma = 0
    for nota in lista_de_notas:
        soma += nota

    quantidade_de_notas = len(lista_de_notas)
    media = soma / quantidade_de_notas
    return media

minhas_notas = [8.5, 7.0, 9.0, 6.5, 8.0]
#minhas_notas_vazia = []

media_calculada = calcular_media(minhas_notas)
#media_calculada_vazia = calcular_media(minhas_notas_vazia)

print(f"A média das minhas notas é: {media_calculada: .2f}")
# print(f"A média das minhas notas vazia é: {media_calculada_vazia: .2f}")
