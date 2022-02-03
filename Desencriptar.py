from FuncoesAuxiliares import *
import os

#Função para desencriptar a mensagem
def desencriptar(p, q, e, msg_cript):
    #Abre a mensagem encriptada
    msg_encriptada = open(msg_cript, 'r')

    #Calcula o d, que é o inverso modular de e mod ((p-1)*(q-1)) e depois o n
    d= inverso_modular_c(e, (p-1) * (q-1))
    n = p*q

    #Transforma cada número encriptado de volta ao número original e salva na lista msg_desencriptada
    msg_desencriptada = []
    for linha in msg_encriptada:
        for palavra in linha.split():
            c = exp_modular(int(palavra), d, n)
            msg_desencriptada.append(c)

    caractere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    codigo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

    #Agora transforma os números em seus respectivos caracteres e salva em uma nova lista -> msg_desencript
    msg_desencript = []
    for i in range(len(msg_desencriptada)):
        for j in range(27):
            if (msg_desencriptada[i] == codigo[j]):
                msg_desencript.append(caractere[j])
    
    #Transforma a lista em uma string
    msg_desencript = lista_String_Nospace(msg_desencript)

    #Salva a mensagem desencriptada no arquivo msg_desencriptada na pasta Arquivos
    try:
        msg_ok = open('ProjetoCriptografiaRSA/Arquivos/msg_desencriptada.txt', 'w')
        msg_ok.write(msg_desencript)
    except:
        if not os.path.exists('ProjetoCriptografiaRSA/Arquivos'):
            os.makedirs('ProjetoCriptografiaRSA/Arquivos')
        msg_ok = open('ProjetoCriptografiaRSA/Arquivos/msg_desencriptada.txt', 'w')
        msg_ok.write(msg_desencript)