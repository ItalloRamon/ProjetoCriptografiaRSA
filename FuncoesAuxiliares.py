from math import sqrt
import os
from re import S
from tabnanny import check
from threading import Timer
from math import sqrt
import time
import random
import PySimpleGUI as sg

#Calcula o MDC entre num1 e num2
def mdc(num1, num2): 
    if (num1 > num2 and num1%num2 == 0): return num2
    else: return mdc(num2, num1%num2)

#Retorna True se num for primo e False se ele não for primo
def eh_primo(num): 
    c = 1
    i = 0
    eh_primo = True
    if (num == 1 or num == 0):
        eh_primo = False

    while (c <= sqrt(num)):
        if (num % c == 0):
            i += 1
            if (i > 1):
                eh_primo = False
                break
        c += 1

    return eh_primo

#Transforma uma lista em uma string. Exemplo: s = ['C','A','R','R','O'], lista_String(s) = C A R R O
def lista_String_space(s): #Transforma uma lista (s) em uma string
    str_teste = ' '
    return str_teste.join(s)

#Transforma uma lista em uma string. Exemplo: s = ['C','A','R','R','O'], lista_String(s) = CARRO
def lista_String_Nospace(s):
    str_teste = ''
    return str_teste.join(s)

#Transforma uma lista de inteiros em uma lista de strings
def lista_int_str(lista_int): 
    lista_str = []
    for int in lista_int:
        lista_str.append(str(int))
    return lista_str

#Gerar número primo
def gerar_primo(janela): 
    primeiros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                        31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103,
                        107, 109, 113, 127, 131, 137, 139,
                        149, 151, 157, 163, 167, 173, 179,
                        181, 191, 193, 197, 199, 211, 223,
                        227, 229, 233, 239, 241, 251, 257,
                        263, 269, 271, 277, 281, 283, 293,
                        307, 311, 313, 317, 331, 337, 347, 349]
    
    #Gerar um número de n bits
    def nbits(n):
        return random.randrange(2**(n-1)+1, 2**n - 1)
    
    def primeiroprimo(n):
        #Pegar um número que não seja dividio por algum da lista de primos
        while True:
            #Gerar um número aleatório
            pc = nbits(n)
    
            #Testar a divisibilidade por todos os números da lista primeiros_primos
            for divisor in primeiros_primos:
                if pc % divisor == 0 and divisor**2 <= pc:
                    break
            else: return pc
    
    def TesteMillerRabin(mrc):
        divisoes_2 = 0
        ec = mrc-1
        while ec % 2 == 0:
            ec >>= 1
            divisoes_2 += 1
        assert(2**divisoes_2 * ec == mrc-1)
    
        def trialComposite(round_tester):
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(divisoes_2):
                if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                    return False
            return True
    
       #Define a quantidade de teste que será feita
        numero_testes = 100000
        for i in range(numero_testes):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True
    
    while True:
        n = 56
        provavel_primo = primeiroprimo(n)
        if not TesteMillerRabin(provavel_primo):
            continue
        else:
            num_primo = provavel_primo
            break

    janela.write_event_value("primo_gerado", num_primo)

#Calculo o inverso modular de 2 números
def inverso_modular_c(n1, n2):
    def mdc(a, b):
        quocientes = []
        if (a < b):
            temp = b
            b = a
            a = temp
        r = a % b
        quocientes.append(a//b)
        while (r != 0):
            a = b
            b = r
            r = a % b
            quocientes.append(a//b)
        return quocientes

    def euclides(a, b):
        if (a % b == 0):
            return b
        return euclides(b, a%b)
        
    mdc = mdc(n1, n2)
    del mdc[-1]
    mdc = list(reversed(mdc))

    x = 0
    c = 1
    fatores = []
    v = 0
    if(len(mdc) == 1):
        fatores.append(-1)
        v = 1
        
    for quociente in mdc:
        r = quociente * c + x
        fatores.append(r)
        temp = c
        c = r
        x = temp
    if (len(fatores) % 2 == 0):
        s = fatores[-2] * -1
        t = fatores[-1]
    else:
        s = fatores[-2]
        t = fatores[-1] * -1

    if(v == 1):
        t *= -1
    
    if (n2 > n1):
        temp = s
        s = t
        t = temp

    cont = 0 
    help_s = s
    while not (n1 <= s and s <= n2):
        if s < n2:
            s += n2
            cont+=1
        elif s > n2:
            s -= n2
            cont+=1
        if cont == 10:
            s = help_s
            break
    return s

#Exponenciação modular rápida
def exp_modular(base, expoente, modulo):
    resultado = 1
    while (expoente > 0):
        if (expoente & 1 == 1):
            resultado = (resultado * base) % modulo
        base = (base * base) % modulo
        expoente >>= 1
    return resultado