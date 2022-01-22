from math import sqrt
import os
from re import S
from tabnanny import check
from threading import Timer
from math import sqrt
import time
import random

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
def lista_String(s): #Transforma uma lista (s) em uma string
    str_teste = ' '
    return str_teste.join(s)

#Transforma uma lista em uma string. Exemplo: s = ['C','A','R','R','O'], lista_String(s) = CARRO
def lista_String_var(s):
    str_teste = ''
    return str_teste.join(s)

#Transforma uma lista de inteiros em uma lista de strings
def lista_int_str(lista_int): 
    lista_str = []
    for int in lista_int:
        lista_str.append(str(int))
    return lista_str

#Gerar número primo
# Large Prime Generation for RSA
## REFAZER ESSA FUNÇAO ##
def gerar_primo(janela): 
    # Pre generated primes
    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                        31, 37, 41, 43, 47, 53, 59, 61, 67,
                        71, 73, 79, 83, 89, 97, 101, 103,
                        107, 109, 113, 127, 131, 137, 139,
                        149, 151, 157, 163, 167, 173, 179,
                        181, 191, 193, 197, 199, 211, 223,
                        227, 229, 233, 239, 241, 251, 257,
                        263, 269, 271, 277, 281, 283, 293,
                        307, 311, 313, 317, 331, 337, 347, 349]
    
    def nBitRandom(n):
        return random.randrange(2**(n-1)+1, 2**n - 1)
    
    def getLowLevelPrime(n):
        '''Generate a prime candidate divisible
        by first primes'''
        while True:
            # Obtain a random number
            pc = nBitRandom(n)
    
            # Test divisibility by pre-generated
            # primes
            for divisor in first_primes_list:
                if pc % divisor == 0 and divisor**2 <= pc:
                    break
            else: return pc
    
    def isMillerRabinPassed(mrc):
        '''Run 20 iterations of Rabin Miller Primality test'''
        maxDivisionsByTwo = 0
        ec = mrc-1
        while ec % 2 == 0:
            ec >>= 1
            maxDivisionsByTwo += 1
        assert(2**maxDivisionsByTwo * ec == mrc-1)
    
        def trialComposite(round_tester):
            if pow(round_tester, ec, mrc) == 1:
                return False
            for i in range(maxDivisionsByTwo):
                if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                    return False
            return True
    
        # Set number of trials here
        numberOfRabinTrials = 100000
        for i in range(numberOfRabinTrials):
            round_tester = random.randrange(2, mrc)
            if trialComposite(round_tester):
                return False
        return True
    

    while True:
        n = 56
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            num_primo = prime_candidate
            break
    janela.write_event_value("p_aleatorio_finalizada", num_primo)

#Calcular o inverso de a mod m
def inverso (a, mod, x): 
    if (mdc(a, mod) != 1):
        return mdc(a, mod)
    
    if ((a * x) % mod == 1):
        return x
    
    return inverso (a, mod, x + 1)

## ARRUMAR ESSA DAQUI ##
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
        
    # n1 = int(input("Digite um número: "))
    # n2 = int(input("Digite outro número: "))
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
    #print(f"Os coeficientes lineares são: {s} e {t}")
    eucli = euclides(n1, n2)
    if (n2 > n1):
        #temp = n1
        #n1 = n2
        #n2 = temp
        temps = s
        s = t
        t = s
    #print(f"{eucli} = {s} * {n1} + {t} * {n2}")
    while not (n1 < s < n2):
        if s < n2:
            s += n2
        elif s > n2:
            s -= n2
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