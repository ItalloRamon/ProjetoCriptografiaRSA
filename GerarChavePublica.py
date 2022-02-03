from FuncoesAuxiliares import *
import os
#Função para gerar a chave pública 
def gerar_chavepublica(p, q, e):
    n = p * q
    try:
        chavepublica = open('ProjetoCriptografiaRSA/Arquivos/chavepublica.txt', 'w')
        chavepublica.write(f'{e} {n}') # chave pública(e, n)
    except:
        if not os.path.exists('ProjetoCriptografiaRSA/Arquivos'):
            os.makedirs('ProjetoCriptografiaRSA/Arquivos')
        chavepublica = open('ProjetoCriptografiaRSA/Arquivos/chavepublica.txt', 'w')
        chavepublica.write(f'{e} {n}') # chave pública(e, n)