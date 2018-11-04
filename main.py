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
    lengthWord = len(bits) + redundancia
    aux = 0
    j = 0
    for i in range(redundancia):
        Hamming = 2**i
        while (aux < Hamming):
            if (aux+1 != Hamming):
                novaPalavra += bits[j]
                j += 1
            else:
                novaPalavra += "-"
            aux += 1
            
            
    
    print("Nova Palavra: " + novaPalavra + "\n")

    impar, dictresultados = verificacao(novaPalavra)
    
    repetidos = [0]*(lengthWord)
    procurados = []
    for i in impar:    
        for j in dictresultados[i].keys():
            repetidos[j-1] += 1
            if repetidos[j-1] == len(impar):
                procurados.append(j)
    print("Indices que se repetem em todos: ", procurados, "\n")
    palavraGerada = ''

    replacebits = list(novaPalavra)
    for i in procurados:
        replacebits[i-1] = "1"
    novaPalavra = ''
    for i in replacebits:
        if (i == "-"):
            novaPalavra += "0"
        else:
            novaPalavra += i
    
    print("Nova Palavra:", novaPalavra, "\n")
    
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
        dictdevalores = {}
        contadorUm = 0
        alternador = 0 
        for i in range(j-1, bitsLength):
            if (alternador == j):
                alternador = 0
                i += j
                continue
            
            dictdevalores[i+1] = bits[i]
            alternador += 1
            
            if bits[i] == "1":
                contadorUm += 1
        contagembits[j] = dictdevalores
        contadoresUM[j] = contadorUm
        
    impares = []

    for i in contadoresUM.keys():
        if (contadoresUM[i] % 2 != 0):
            impares.append(i)

    

    print("Verificação\n")
    for i in contagembits.keys(): 
        print("Bit "+str(i)+":", contagembits[i])

    print("\nContagem de Verificação:\n")
    for i in contadoresUM.keys():
        print(str(i)+":", contadoresUM[i])

    print()
    print("Impares: " +  str(impares) + "\n")

    return impares, contagembits

def main():
    bits = input("\nDigite a palavra a ser enviada: ")
    print()
    geracao(bits) #1111000010101110


main()