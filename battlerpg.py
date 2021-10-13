# BattleRPG.py v0.1 Alpha
# Author: zarkus

# Importações
import os

# Variáveis globais
vida_monstro = 100
vida_jogador = 100
dano_monstro = 0

# Funções
def pular():
    print("")

def limpar_console():
    os.system("cls" if os.name == "nt" else "clear")

def poderes_jogador(power):
    if power == "Q":
        dano_jogador = 20


# Função principal
def main():

    contador = 0
    while contador == 0:
        jogador = str(input("Nome do jogador: "))
        pular()
        
        print("Elaner: {} de vida".format(vida_monstro))
        print("{}: {} de vida".format(jogador, vida_jogador))
        pular()

        print("""Q - Bola de Fogo
        W - Cometa Arcano
        E - Explosão Vulcânica""")
        escolha_poder = int(input("Escolha: "))



        opcao = int(input("Deseja parar de jogar? (1 - sim / 2 - não): "))

        while opcao != 1 and opcao != 2:
            print("Escolha inválida, tente novamente")
            opcao = int(input("Deseja parar de jogar? (1 - sim / 2 - não): "))
            
        if opcao == 1:
            contador = 1
        elif opcao == 2:
            limpar_console()
            continue

# Executa o programa
main()
