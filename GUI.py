import PySimpleGUI as sg
import sys
import threading
from FuncoesAuxiliares import *
import pyperclip
from GerarChavePublica import *
from random import randint
from Encriptar import *
from Desencriptar import *

#Cria toda a interface gráfica
def interface_grafica():
    # Tema
    sg.theme("Dark")

    #Tela que aparece o número p gerado aleatoriamente
    def tela_p_aleatorio(p_aleatorio):
        #Tema
        sg.theme("Dark")
        #Layout
        layout = [
            [sg.Text(p_aleatorio)],
            [sg.Button("Copiar")]
        ]
        #Janela
        janela = sg.Window("Title", layout)
        #Ler dados
        while True:
            evento, dados = janela.Read()
            if (evento == sg.WIN_CLOSED):
                janela.close()
                break
            if (evento == "Copiar"):
                pyperclip.copy(p_aleatorio)
            
    #Janela 1
    def criar_janela1():
        layout_janela1 = [
            [sg.Text("Bem vindo (a) ao Encriptador de Mensagens RSA")],
            [sg.Text("Selecione uma das 3 opções")],
            [sg.Button("Gerar Chave Pública", key="gerar_chave_publica", size=(35,1))],
            [sg.Button("Encriptar Mensagem", key="encriptar_msg", size=(35,1))],
            [sg.Button("Desencriptar Mensagem", key="desencriptar_msg", size=(35,1))]
        ]
        return sg.Window("EM-RSA", layout_janela1, finalize=True)

    #Janela 2
    def criar_janela_chavepublica():
        layout_janela_chaveoublica = [
            [sg.Text("Digite um número primo (p)")],
            [sg.Input(key="p"), sg.Button("Aleatório", key="p_aleatorio")],
            [sg.Text("Digite outro número primo (q)")],
            [sg.Input(key="q"), sg.Button("Aleatório", key="q_aleatorio")],
            [sg.Text("Digite um número (e) coprimo a (p-1) * (q-1): ")],
            [sg.Input(key="e"), sg.Button("Aleatório", key="e_aleatorio")],
            [sg.Button("Gerar Chave Pública", key="gerar"), sg.Button("Voltar")]
        ]
        return sg.Window("Gerar Chave Pública", layout_janela_chaveoublica, finalize=True)

    #Janela 3
    def criar_janela_encriptar():
        layout_janela_encriptar = [
            [sg.Text("Digite a chave pública (n):")],
            [sg.Input(size=(48,1), key="n")],
            [sg.Text("Digite a chave pública (e):")],
            [sg.Input(size=(48,1), key="e")],
            [sg.Text("Digite a mensagem para ser criptografada (APENAS letras):")],
            [sg.Multiline(autoscroll=True, size=(48, 5), key="msg")],
            [sg.Button("Encriptar", key="encriptar"), sg.Button("Voltar")]
        ]
        return sg.Window("Encriptar Mensagem", layout_janela_encriptar, finalize=True)

    #Janela 4
    def criar_janela_desencriptar():
        layout_janela_desencriptar = [
            [sg.Text("Digite o número primo (p): ")],
            [sg.Input(key="p")],
            [sg.Text("Digite o número primo (q): ")],
            [sg.Input(key="q")],
            [sg.Text("Digite a  chave pública (e): ")],
            [sg.Input(key="e")],
            [sg.Text("Selecione um arquivo com a mensagem encriptada:")],
            [sg.Input(key="caminho_arquivo")],
            [sg.FileBrowse("Selecionar arquivos", target="caminho_arquivo", file_types=(("Arquivos de Texto", "*.txt"),))],
            [sg.Button("Desencriptar", key="desencriptar"), sg.Button("Voltar")]
        ]
        return sg.Window("Desencriptar Mensagem", layout_janela_desencriptar, finalize=True)
        
    #Janelas
    janela1, janela2, janela3, janela4 = criar_janela1(), None, None, None

    #Ler valores
    while True:
        janela, evento, valores = sg.read_all_windows()
        if (evento == sg.WIN_CLOSED):
            janela.close()
            sys.exit()
        
        elif (evento == "gerar_chave_publica") and (janela == janela1):
            janela1.hide()
            janela2 = criar_janela_chavepublica()
        
        elif (evento == "p_aleatorio") and (janela == janela2):
            thread_p_aleatorio = threading.Thread(target=gerar_primo, args=(janela,), daemon=True)
            thread_p_aleatorio.start()
        elif (evento == "primo_gerado"):
            thread_p_aleatorio.join()
            tela_p_aleatorio(valores["primo_gerado"])
        
        elif (evento == "q_aleatorio") and (janela == janela2):
            thread_q_aleatorio = threading.Thread(target=gerar_primo, args=(janela,), daemon=True)
            thread_q_aleatorio.start()
        elif (evento == "primo_gerado"):
            thread_q_aleatorio.join()
            tela_p_aleatorio(valores["primo_gerado"])

        elif (evento == "e_aleatorio"):
            p = int(valores["p"])
            q = int(valores["q"])
            φ = (p - 1)*(q - 1)
            while True:
                e = randint(2, φ-1)
                if mdc(e, φ) == 1:
                    break
            tela_p_aleatorio(e)

        elif (evento == "gerar"):
            p = int(valores["p"])
            q = int(valores["q"])
            e = int(valores["e"])
            
            gerar_chavepublica(p, q, e)
            sg.popup_no_border("Chave pública gerada com sucesso")
        
        elif (evento == "encriptar_msg"):
            janela.hide()
            janela3 = criar_janela_encriptar()
        
        elif(evento == "encriptar"):
            n = int(valores["n"])
            e = int(valores["e"])
            msg = valores["msg"]
            encriptar(n, e, msg)
            sg.popup_no_border("Mensagem Encriptada com sucesso!")
        
        elif (evento == "desencriptar_msg"):
            janela.hide()
            janela4 = criar_janela_desencriptar()
        
        elif (evento == "desencriptar"):
            p = int(valores["p"])
            q = int(valores["q"])
            e = int(valores["e"])
            msg_cript  = valores["caminho_arquivo"]
            desencriptar(p, q, e, msg_cript)
            sg.popup_no_border("Mensagem desencriptada com sucesso!")

        elif (evento == "Voltar" and janela == janela2):
            janela1.UnHide()
            janela2.close()
        elif (evento == "Voltar" and janela == janela3):
            janela1.UnHide()
            janela3.close()
        elif (evento == "Voltar" and janela == janela4):
            janela1.UnHide()
            janela4.close()