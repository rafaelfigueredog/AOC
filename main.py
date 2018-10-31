from math import sqrt

def calculaBitsverificacao(m): 
    expoente = 0
    resultado = 0
    while (resultado != m):
        resultado = 2**expoente
        expoente += 1 
    return expoente



def geracao():

    bits = input()
    novaPalavra = ''
    bitsLength = calculaBitsverificacao(len(bits))
    

    potencias = []

    for i in range(bitsLength):
        if (2**i <= bitsLength):
            potencias.append(2**i)
    
"""     for i in range(bitsLength):
        if ()
        novaPalavra +=  """
        



def verificacao():

    bits = input()
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

    print(contadoresUM)

    for i in contagembits.items(): 
        print(i)
        
    print(impares)

print(calculaBitsverificacao(8))
print(calculaBitsverificacao(16))
print(calculaBitsverificacao(32))
print(calculaBitsverificacao(64))