def gerar_primo(janela):
    # def exitfunc():
    #     os._exit(0)

    # def primos(n):
    #     sieve = [True] * n
    #     for i in range(3,int(n**0.5)+1,2):
    #         if sieve[i]:
    #             sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    #     return [2] + [i for i in range(3,n,2) if sieve[i]]

    # start_time = time.time()
    # Timer(60, exitfunc).start()

    # lista_primos = primos(100000000)
    # random_num = random.randint(0, 100) * -1

    first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
					31, 37, 41, 43, 47, 53, 59, 61, 67,
					71, 73, 79, 83, 89, 97, 101, 103,
					107, 109, 113, 127, 131, 137, 139,
					149, 151, 157, 163, 167, 173, 179,
					181, 191, 193, 197, 199, 211, 223,
					227, 229, 233, 239, 241, 251, 257,
					263, 269, 271, 277, 281, 283, 293,
					307, 311, 313, 317, 331, 337, 347, 349]
    def getLowLevelPrime(n):
        '''Generate a prime candidate divisible
        by first primes'''
        while True:
            # Obtain a random number
            #pc = nBitRandom(n)
            pc = random.getrandbits(n)
            # Test divisibility by pre-generated
            # primes
            for divisor in first_primes_list:
                if pc % divisor == 0 and divisor**2 <= pc:
                    break
            else: return pc

    def isPrime(n, k):
        if (n<=1 or n==4):
            return False
        
        if (n == 2 or n==3):
            return True
        
        #Encontrar o d n-1 = d * 2^r
        d = n -1
        while (d % 2 == 0):
            d = d // 2
        
        for i in range(k):
            if (millerTeste(d, n) == False):
                return False
        return True
    
    def millerTeste(n, d):
        a = random.randint(2,n-2)
        x = pow(a,d,n)
        if (x == 1) or (x == n-1):
            return True
        
        while (d != n - 1):
            x = (x * x) % n
            d *= 2
            if (x == 1):
                return False
            if (x == n-1):
                return True
                
    num_primo = getLowLevelPrime(2)
    check = isPrime(num_primo, 1)
    while check == False:
        num_primo = getLowLevelPrime(2)
        check = isPrime(num_primo, 1)
        
    
    # num_primo = lista_primos[random_num]
    janela.write_event_value("p_aleatorio_finalizada", num_primo)