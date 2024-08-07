def computador_escolhe_jogada(n, m):
    x = 0
    while x < m:
        x = x + 1
        y = n - x
        if y % (m + 1) == 0:
            return int(x)
            break
    if y % (m + 1) != 0:
        return int(m)

def usuario_escolhe_jogada(n, m):
    x = int(input("\nQuantas peças você vai tirar? "))
    passagem = False
    while not passagem: 
        if x < 1 or x > m:
            print("\nOops! Jogada inválida! Tente de novo.")
            x = int(input("\nQuantas peças você vai tirar? "))
        else:
            return int(x)
  
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m + 1) == 0:
        print("Você começa!")
        while n != 0 and n > 0:
            if n != 0:
                u = usuario_escolhe_jogada(n, m)
                n = n - u
                print("\nVocê tirou", u, "peças")
                print("\nAgora restam", n, "peças no tabuleiro")
            c = computador_escolhe_jogada(n, m)
            n = n - c
            print("\nO computador tirou", c, "peças")
            print("\nAgora restam", n, "peças no tabuleiro")
    else:
        print("Computador começa")
        while n != 0 and n > 0:
            c = computador_escolhe_jogada(n, m)
            n = n - c
            print("\nO computador tirou", c, "peças")
            print("\nAgora restam", n, "peças no tabuleiro")
            if n != 0:
                u = usuario_escolhe_jogada(n, m)
                n = n - u
                print("\nVocê tirou", u, "peças")
                print("\nAgora restam", n, "peças no tabuleiro")
    
    print("\nFim de jogo! O computador ganhou!\n")

def campeonato():
    print("**** Rodada 1 ****\n")
    partida()
    print("**** Rodada 2 ****\n")
    partida()
    print("**** Rodada 3 ****\n")
    partida()
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X 3 Computador")        

print ("Bem-vindo ao jogo do NIM! Escolha:")

print()

x = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato\n"))

if x == 1:
    partida()
else:
    campeonato()