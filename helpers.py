import random
from setings import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRA_SECRETA


def gerar_palavra_secreta():
    """
    Função que escolhe uma palavra randomicamente dentro
    do arquivo 'dados.txt'.
    :return: string (palavra secreta).
    """
    with open(ARQUIVO_PALAVRA_SECRETA, 'r') as f_obj:
        palavras = f_obj.read().splitlines()

    return random.choice(palavras)


def verificar_letra_informada(palavra_secreta, suas_tentativas, tentativa):
    """
    - Função verifica se a letra informada está correta.
    :param palavra_secreta: Gerada com base no arquivo dados.txt.
    :param suas_tentativas: Lista com todas as tentativas.
    :param tentativa: Letra inserida na jogada atual.
    :return: Retorna um status.
    """
    status = ''  # O status precisa ser zerado sempre que a função for chamada.
    acertos = 0  # Também precisa ser zerado a cada jogada/tentativa.
    ultima_letra = ' '

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra
            ultima_letra = letra
        else:
            status += '*'

        if letra.lower() == tentativa.lower():
            acertos += 1
    print(f"- Bom chute!!! {acertos} letra(s) '{tentativa.upper()}'")
    """
    if ultima_letra.lower() in palavra_secreta:
        print(f"- Bom chute!!! {acertos} letra(s) '{tentativa.upper()}'")
    else:
        print(f"- Você errou!!! Nenhuma letra '{tentativa.upper()}'")
    """
    return status


def total_tentativas(palavra_secreta):
    """
    - Define o número de tentativas de acordo com o tamanho da palavra secreta.
    :param palavra_secreta: Gerada randomicamente.
    :return: Quantidade de tentativas.
    """
    chances = len(palavra_secreta)

    return chances + TENTATIVAS_ADICIONAIS


def jogo(palavra_secreta):
    """
    - Função principal do jogo.
    :param palavra_secreta: Palavra secreta obtida do arquivo dados.txt.
    :return:
    """
    chute = 0
    acertou = False
    suas_tentativas = []
    chances = total_tentativas(palavra_secreta)
    total_chances = chances

    print(f"- Total de chances: {chances}")

    while chute < total_chances:
        letra_tentativa = input("\nDigite uma letra: ")

        # Diminuindo as chances usadas
        chances -= 1

        # Se a letra já foi informada ou adivinhada
        if letra_tentativa in suas_tentativas:
            print("*** ATENÇÃO ***")
            print("Você já usou essa letra!!! -1 chance.")

        elif len(letra_tentativa) == 1:
            # Adicionando as letras no local correto.
            suas_tentativas.append(letra_tentativa)
            resultado = verificar_letra_informada(palavra_secreta,
                                                  suas_tentativas,
                                                  letra_tentativa)
            if resultado == palavra_secreta:
                acertou = True
                print("\n****** Parabéns você acertou!!! ******")
                print(f"A palavra secreta é: {palavra_secreta.upper()}")
                break
            else:
                print("\nPalavra secreta")
                print(f"- {' '.join(resultado)}")
        else:
            print("\nOOPS!!! Digite apenas uma letra por tentativa.")

        # Mostra quantas tentativas ainda restam.
        print(f"\n- Ainda restam {chances} tentativas")
        chute += 1

    if chute == total_chances:
        print("\n#### Suas tentativas acabaram... ####")
        print("Você perdeu...")
        print(f"A palavra secreta era '{palavra_secreta.upper()}'")
