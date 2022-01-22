from FuncoesAuxiliares import *
## ADICIONAR COMENTÀRIOS AQUI ##
def desencriptar(p, q, e, msg_cript):
    msg_encriptada = open(msg_cript, 'r')

    d= inverso_modular_c(e, (p-1) * (q-1))
    n = p*q

    msg_desencriptada = []
    for linha in msg_encriptada:
        for palavra in linha.split():
            #c = pow(int(palavra), d, n)
            c = exp_modular(int(palavra), d, n)
            msg_desencriptada.append(c)

    caractere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    codigo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

    msg_desencript = []
    for i in range(len(msg_desencriptada)):
        for j in range(27):
            if (msg_desencriptada[i] == codigo[j]):
                msg_desencript.append(caractere[j])
    
    msg_desencript = lista_String_var(msg_desencript)

    msg_ok = open('ProjetoCriptografia/Arquivos/msg_desencriptada.txt', 'w')
    msg_ok.write(msg_desencript)