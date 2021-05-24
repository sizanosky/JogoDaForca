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