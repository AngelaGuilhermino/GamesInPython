import random # Possibita gerar valores aletórios

opcoes = ["pedra", "papel", "tesoura"]
jogador = input("Digite pedra, papel ou tesoura: ")
computador = random.choice(opcoes) # Escolhe aleatoriamente os valores dentro da variável

print(f"Você escolheu: {jogador}")
print(f"O computador escolheu: {computador}")

# Condições para resultado do partida
if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
    (jogador == "tesoura" and computador == "papel") or \
    (jogador == "papel" and computador == "pedra"):
    print("Você venceu!")
else:
    print("Computador venceu!")