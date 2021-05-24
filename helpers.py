import random
from setings import TENTATIVAS_ADICIONAIS, ARQUIVO_PALAVRA_SECRETA


def gerar_palavra_secreta():
    """
    - Função que escolhe uma palavra randomicamente dentro
    do arquivo dados.txt
    :return: Palavra secreta.
    """
    with open(ARQUIVO_PALAVRA_SECRETA, 'r') as f_obj:
        palavra = f_obj.read().splitlines()

    return random.choice(palavra)


def verificar_palavra_informada(palavra_secreta, suas_tentativas, tentativa):
    """
    - Função verifica se a letra informada está correta.
    :param palavra_secreta: Gerada com base no arquivo dados.txt.
    :param suas_tentativas: Lista com todas as tentativas.
    :param tentativa: Letra inserida na jogada atual.
    :return: Retorna um status.
    """
    status = ''  # O status precisa ser zerado sempre que a função for chamada.
    acertos = 0  # Também precisa ser zerado a cada jogada/tentativa.

    for letra in palavra_secreta:
        if letra.lower() in suas_tentativas:
            status += letra
        else:
            status += '*'

        if letra.lower() == tentativa.lower():
            acertos += 1

    print(f"\n- Acertou {acertos} letras '{tentativa}'")

    return status


def total_tentativas(palavra_secreta):
    """
    - Define o número de tentativas de acordo com o tamanho da palavra secreta.
    :param palavra_secreta: Gerada randomicamente.
    :return: Quantidade de tentativas.
    """
    chances = len(palavra_secreta)

    return chances + TENTATIVAS_ADICIONAIS
