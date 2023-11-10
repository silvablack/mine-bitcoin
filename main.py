from hashlib import sha256
import time

zeros = 8


def hash(texto):
    return sha256(texto.encode('ascii')).hexdigest()


def minerar(num_bloco, transacoes, hash_anterior, zeros):
    qtd_zeros = "0" * zeros
    nao_achei = True
    nonce = 0

    while nao_achei:
        hash_bloco = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        hash_atual = hash(hash_bloco)
        nonce += 1

        if hash_atual.startswith(qtd_zeros):
            nao_achei = False
            print(f'\nAté que enfim, NONCE encontrado {nonce}\n')
            return hash_atual


transacoes = """
PEDRO 50 > PAULO 10
"""

if __name__ == '__main__':
    inicio = time.time()
    print(f'\nInicio da mineração\n')
    minerar(816189, transacoes, "95226740942c99bca92d99602829db0da5e357d1ef6d8aad10be9c5b14438ee0", zeros)
    total = str((time.time() - inicio))
    print(f'\nFim da mineracao: {total} \n')
