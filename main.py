from math import sqrt

def calculaBitsverificacao(m): 
    expoente = 0
    resultado = 0
    while (resultado != m):
        resultado = 2**expoente
        expoente += 1 
    return expoente

#1111000010101110
def geracao(bits):

    redundancia = calculaBitsverificacao(len(bits))
    novaPalavra = ''
    lengthWord = len(bits) + redundancia
    aux = 0
    j = 0
    for i in range((redundancia+1)):
        Hamming = 2**i
        while (aux < Hamming):
            if (aux == lengthWord):
                break
            if (aux+1 != Hamming):
                novaPalavra += bits[j]
                j += 1
            else:
                novaPalavra += "-"
            aux += 1
        
    print("Nova Palavra: " + novaPalavra + "\n")

    impar, dictresultados = verificacao(novaPalavra)
    
    """ repetidos = [0]*(lengthWord)
    procurados = []

    for i in impar:    
        for j in dictresultados[i].keys():
            repetidos[j-1] += 1
            if repetidos[j-1] == len(impar):
                procurados.append(j)
    print("Indices que se repetem em todos: ", procurados, "\n") """
    
    palavraGerada = ''
    replacebits = list(novaPalavra)
    for i in impar:
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

    i = 0
    while 2**i <= bitsLength:
            potencias.append(2**i)
            i+=1

    contagembits = {}
    contadoresUM = {}

    for j in potencias:
        dictdevalores = {}
        contadorUm = 0
        alternadorpos = 0
        i = j-1
        while (i < bitsLength):
            if (alternadorpos == j):
                alternadorpos = 0
                i += j
                continue
            
            dictdevalores[i+1] = bits[i]
            alternadorpos += 1
            if bits[i] == "1":
                contadorUm += 1
            
            i += 1
        contagembits[j] = dictdevalores
        contadoresUM[j] = contadorUm

    # até aqui, fez toda a separação por bits de potencia de 2. 

    impares = []

    for i in contadoresUM.keys():
        if (contadoresUM[i] % 2 != 0):
            impares.append(i)

    # Paridade impar identificada.

    print("\n\nVerificação\n")
    for i in contagembits.keys(): 
        print("Bit "+str(i)+":", contagembits[i])

    print("\nContagem de Verificação:\n")
    for i in contadoresUM.keys():
        print(str(i)+":", contadoresUM[i])

    print()
    print("Impares: " +  str(impares) + "\n")

    for i in impares:
        for j in list(contagembits[].keys()).sort():
            if 

    return impares, contagembits

def main():
    
    while(True):

        print("\n     Hamming Aplicação    ")
        print()
        print("1 - Gerar")
        print("2 - Verificar")
        print("0 - Sair")
        print()

        opcao = input('# ')
        

        if (opcao == '1'):
            print("Palavra: ", end='')
            bits = input()
            geracao(bits)
        elif (opcao == '2'):
            print("Palavra: ", end='')
            bits = input()
            verificacao(bits)
        elif (opcao == '0'):
            print("Saindo...")
            break
        else:
            print('\033[31m'+'\n    Opção Invalida!\n'+'\033[0;0m')
            

main()