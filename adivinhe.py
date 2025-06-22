numero_secreto = 42
palpite = input("Qual é seu palpite?")
while palpite != numero_secreto:
    palpite_srt = input("Adivinhe o número de 1 a 100:")
    palpite = int(palpite_srt)
    if palpite < numero_secreto: print("Seu palpite foi muito BAIXO! Tente um número maior.")
    elif palpite > numero_secreto: print("Seu palpite foi muito ALTO! Tente um número menor.")
    else:print(f"Parabéns! Você acertou! O numero sereto era {numero_secreto}.")
    
print("Fim do jogo!")
