from math import sqrt

def binary_search_ite(vet, num):
	esquerda, direita, tentativa = 0, len(vet), 1
	while 1:
		meio = (esquerda + direita) // 2
		aux_num = vet[meio]
		if num == aux_num:
			return tentativa
		elif num > aux_num:
			esquerda = meio
		else:
			direita = meio
		tentativa += 1

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
            novaPalavra += bits[j]
            aux += 1
            j += 1
        novaPalavra += "-"
    
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