from FuncoesAuxiliares import *

#Função para gerar a chave pública 
def gerar_chavepublica(p, q, e):
    n = p * q

    chavepublica = open('ProjetoCriptografiaRSA/Arquivos/chavepublica.txt', 'w')
    chavepublica.write(f'{e} {n}') # chave pública(e, n)
