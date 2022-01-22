from FuncoesAuxiliares import *

def encriptar(n, e, msg1):
    
    #msg = input("Digite a mensagem para ser criptografada: ").upper()
    
    msg_precod = []
    caractere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
    codigo = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    msg=[]
    for i in range(len(msg1)):
        for j in range(27):
            if (msg1[i] == caractere[j].lower() or msg1[i] == caractere[j]):
                msg.append(caractere[j])
    msg = lista_String_var(msg)
    

    ## Pega uma letra da mensagem e compara com todos os caracteres, se for igual adicona seu respectivo número na lista msg_precod
    for i in range(len(msg)):
        for j in range(27): 
            if (msg[i] == caractere[j]): 
                msg_precod.append(codigo[j])

    
    #n = int(input("Digite a chave pública (n): "))
    #e = int(input("Digite a chave pública (e): "))

    msg_cod = []
    for num in msg_precod:
        #c = pow(num, e, n)
        c = exp_modular(num, e, n)
        msg_cod.append(c)

    msg_cod = lista_int_str(msg_cod)
    msg_cod = lista_String(msg_cod)

    msg_encriptada = open('ProjetoCriptografia/Arquivos/msg_encriptada.txt', 'w')
    msg_encriptada.write(msg_cod)
