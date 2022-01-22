from FuncoesAuxiliares import *
 
def gerar_chavepublica(p, q, e):
    #while True:
        #p = int(input('Digite um número PRIMO para p: '))
        #q = int(input('Digite um número PRIMO para q: '))
 
        #if eh_primo(p) and eh_primo(q): break
        #else: print(f'{p} e/ou {q} NÃO SÃO PRIMOS!\nPOR FAVOR digite novamente\n')
 
    n = p * q
    #φ = (p - 1)*(q - 1)
 
    #while True:
        #e = int(input(f'Informe um número e que seja 1 < e < {φ} e o mdc(e, {φ}) = 1: '))
 
        #if (1 < e < φ) and (mdc(e, φ) == 1): break
        #else: print(f'O número {e} não atende aos critérios exigidos!\n')
 
    chavepublica = open('ProjetoCriptografia/Arquivos/chavepublica.txt', 'w')
    chavepublica.write(f'{e} {n}') # chave pública(e, n)

