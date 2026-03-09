print("Seja bem-vindo(a)")
resposta = input("Quer começar? (S/N) ").upper()

if resposta != "S":
    quit()
    
pontos = 0

print("Começando...")
print("Qual a tipagem do Pikachu? \n A) Elétrico \n B) Metal e normal \n C) Metal \n D) Elétrico e normal")
resposta1 = input("Digite sua resposta: ")

if resposta1 == "A":
    print("Correto!")
    pontos = pontos + 1
else:
    print("Incorreto")
    
print("Qual o nome do Deus pokémon? \n A) Mew \n B) Palkia \n C) Arceus \n D) Lugia")
resposta2 = input("Digite sua resposta: ")

if resposta2 == "C":
    print("Correto!")
    pontos = pontos + 1
else:
    print("Incorreto")
    
print("Qual tipagem NÃO existe? \n A) Voador \n B) Lutador \n C) Sombrio \n D) Luz")
resposta3 = input("Digite sua resposta: ")

if resposta3 == "D":
    print("Correto!")
    pontos = pontos + 1
else:
    print("Incorreto")
    
print(f"Quiz finalizado!! Sua pontuação foi de: {pontos}/3!")
