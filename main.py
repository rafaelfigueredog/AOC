from math import sqrt

def calculaBitsverificacao(m): 
    expoente = 0
    resultado = 0
    while (resultado != m):
        resultado = 2**expoente
        expoente += 1 
    return expoente



def geracao(bits):

    redundancia = calculaBitsverificacao(len(bits))
    novaPalavra = ''
    expoente = 0
    aux = 0
    j = 0
    for i in range(redundancia):
        Hamming = 2**i
        while (aux < Hamming):
            novaPalavra += bits[j]
            aux += 1
            j += 1
        novaPalavra += "-"
    
    print("Nova Palavra: " + novaPalavra + "\n")

    verificacao(novaPalavra)

    

    return novaPalavra
   

def verificacao(bits):

    bitsLength = len(bits)
    potencias = []

    for i in range(bitsLength):
        if (2**i <= bitsLength):
            potencias.append(2**i)
    contagembits = {}
    contadoresUM = {}
    for j in potencias:
        listadevalores = []
        contadorUm = 0
        alternador = 0 
        for i in range(j-1, bitsLength):
            if (alternador == j):
                alternador = 0
                i += j
                continue
            
            listadevalores.append(bits[i])
            alternador += 1
            
            if bits[i] == "1":
                contadorUm += 1
        contagembits[j] = listadevalores
        contadoresUM[j] = contadorUm
        
    impares = []

    for i in contadoresUM.keys():
        if (contadoresUM[i] % 2 != 0):
            impares.append(i)

    

    print("Verificação\n")
    for i in contagembits.items(): 
        print(i)

    print("\nContagem\n")
    print(contadoresUM)
    print()
    print("Impares: " +  str(impares) + "\n")
bits = input("\nDigite a palavra a ser enviada: ")
print()
geracao(bits) #1111000010101110