from GerarChavePublica import *
from Encriptar import *
from Desencriptar import *
import GUI
# print('''
#                        _                              _           
#                       | |                            | |          
#   ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
#  / __| '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
# | (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
#  \___|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
#             __/ | |              __/ |         | |           __/ |
#            |___/|_|             |___/          |_|          |___/ 
# ''')

# while True:
#     print('''Selecione uma das 3 opções:
#     (1) - Gerar chave pública
#     (2) - Encriptar uma mensagem
#     (3) Desencriptar uma mensagem
#     (999) Fechar o programa''')

#     escolha = int(input("Qual opção desejada: "))
#     if (escolha == 1):
#         gerar_chavepublica()
#     elif (escolha == 2):
#         n=int(input("n: "))
#         e=int(input("e: "))
#         msg=input("msg: ")
#         encriptar(n, e, msg)
#     elif (escolha == 3):
#         desencriptar()
#     elif (escolha == 999):
#         break
#     else:
#         print("Digite uma opção válida!")
    
#     print('')
GUI.interface_grafica()