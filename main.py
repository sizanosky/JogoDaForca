"""
* Módulo 20 - Jogo da forca
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 24/05/2021
* Programa em Python 3 para simular o Jogo da Forca.
"""

from helpers import *
from time import sleep

print("Hello World!")

if __name__ == "__main__":
    print("\n+*=*+*=*+*=*+ Jogo da Forca +*=*+*=*+*=*+")
    sleep(1)
    print(f"{41 * '*'}")

    # Chama a função e armazena em uma variável
    palavra_secreta = gerar_palavra_secreta().upper()
    print("\nSorteando palavra.\n")
    sleep(1)
    print("\nSorteando palavra..\n")
    sleep(1)
    print("\nSorteando palavra...\n")
    sleep(1)
    print("A palavra é:")

    for letra in palavra_secreta:
        print("*", end=" ")

    print(f"\n{'_' * len(palavra_secreta)}")

    # Calculando o tamanho da palavra
    tamanho_palavra = len(palavra_secreta)
    print(f"- A palavra tem {tamanho_palavra} letras")

    jogo(palavra_secreta)
