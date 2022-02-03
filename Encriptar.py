from FuncoesAuxiliares import *

#Função para Encriptar a mensagem
def encriptar(n, e, msg_usuario):
    
    caractere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    codigo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    
    # Transforma toda as letras da mensagem em letras maiúsculas
    msg_upper=[] 
    for i in range(len(msg_usuario)):
        for j in range(27):
            if (msg_usuario[i] == caractere[j].lower() or msg_usuario[i] == caractere[j]):
                msg_upper.append(caractere[j])
    msg_upper = lista_String_Nospace(msg_upper)
    

    ## Pega uma letra da mensagem e compara com todos os caracteres, se for igual adicona seu respectivo número na lista msg_precod
    msg_precod = []
    for i in range(len(msg_upper)):
        for j in range(27): 
            if (msg_upper[i] == caractere[j]): 
                msg_precod.append(codigo[j])

    # Transforma cada número da mensagem pré-codificada
    msg_cod = []
    for num in msg_precod:
        c = exp_modular(num, e, n)
        msg_cod.append(c)

    #Converte a mensagem codificada de uma lista de inteiros para uma lista de string, e depois transforma a lista em uma string
    msg_cod = lista_int_str(msg_cod)
    msg_cod = lista_String_space(msg_cod)

    #Salva a mensagem encriptada no arquivo msg_encriptada dentro da pasta Arquivos
    msg_encriptada = open('ProjetoCriptografiaRSA/Arquivos/msg_encriptada.txt', 'w')
    msg_encriptada.write(msg_cod)
