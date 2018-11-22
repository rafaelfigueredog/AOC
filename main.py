from math import sqrt

def calculaPotencias(size): 
    potencias = []
    i = 0
    while 2**i <= size:
            potencias.append(2**i)
            i+=1
    return potencias

def calculaRedundancia(m): 
    expoente = 0
    resultado = 0
    while (resultado != m):
        resultado = 2**expoente
        expoente += 1 
    return expoente

def ConstrutorPalavra(palavra, condicao): 
    
    # Sobre a condição
    # True para Enviar (Aumenta o tamanho)
    # False pra Verificar (retorna a palavra sem a redundancia)

    if condicao:
        pass
    else:
        pass

def contadorParidade(contadoresUM):

    impares = []
    pares = []
    for i in contadoresUM.keys():
        if (contadoresUM[i] % 2 != 0):
            impares.append(i)
        else:
            pares.append(i)

    return impares, pares


def SeparacaoPorBits(palavra, size):

    potencias = calculaPotencias(size)

    contagembits = {}
    contadoresUM = {}

    for j in potencias:
        dictdevalores = {}
        contadorUm = 0
        alternadorpos = 0
        i = j-1
        while (i < size):
            if (alternadorpos == j):
                alternadorpos = 0
                i += j
                continue
            
            dictdevalores[i+1] = palavra[i]
            alternadorpos += 1
            if palavra[i] == "1":
                contadorUm += 1
            
            i += 1
        contagembits[j] = dictdevalores
        contadoresUM[j] = contadorUm

    return contagembits, contadoresUM

def geracao(palavra):

    redundancia = calculaRedundancia(len(palavra))
    novaPalavra = ''
    lengthWord = len(palavra) + redundancia
    aux = 0
    j = 0
    for i in range((redundancia+1)):
        Hamming = 2**i
        while (aux < Hamming):
            if (aux == lengthWord):
                break
            if (aux+1 != Hamming):
                novaPalavra += palavra[j]
                j += 1
            else:
                novaPalavra += "-"
            aux += 1
        
    print("Nova Palavra: " + novaPalavra + "\n")

    contagembits, contadoresUM = SeparacaoPorBits(novaPalavra, lengthWord)

    impares, par = contadorParidade(contadoresUM)
    #impar, dictresultados = verificacao(novaPalavra)

    print("\n\nVerificação\n")
    for i in contagembits.keys():
        print("Bit " + str(i) + ":", contagembits[i])

    print("\nContagem de Verificação:\n")
    for i in contadoresUM.keys():
        print(str(i) + ":", contadoresUM[i])

    print()
    print("Impares: " + str(impares))

    palavraGerada = ''
    replacebits = list(novaPalavra)
    for i in impares:
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

    size = len(bits)

    contagembits, contadoresUM = SeparacaoPorBits(bits, size)

    # até aqui, fez toda a separação por bits de potencia de 2. 

    impares, pares = contadorParidade(contadoresUM)

    # Paridade impar identificada.

    print("\n\nVerificação\n")
    for i in contagembits.keys(): 
        print("Bit "+str(i)+":", contagembits[i])

    print("\nContagem de Verificação:\n")
    for i in contadoresUM.keys():
        print(str(i)+":", contadoresUM[i])

    print()
    print("Impares: " +  str(impares))

    # Impressão de informações
    verificacao1 = (size+1)*[0]
    maior = 0
    for i in impares:
        listaValores = list(contagembits[i].keys())
        for j in listaValores:
            verificacao1[j] += 1
            if verificacao1[j] > maior:
                maior = verificacao1[j]
    
    # encontrei repetidos até aqui. 

    candidatosErro = []
    for i in range(len(verificacao1)):
        if verificacao1[i] == maior:
            candidatosErro.append(i)
    
    print("Candidatos a Erro:", candidatosErro)

    verificacao2 = (size+1)*[0]
    for i in pares:
        listaValores = list(contagembits[i].keys())
        for j in listaValores:
            verificacao2[j] += 1
    
    idxBitError = -1
    for i in candidatosErro:
        if verificacao2[i] == 0:
            idxBitError = i

    print("Bit Errado:", idxBitError)

    potencias = calculaPotencias(size)

    fixpalavra = []
    for i in bits:
        fixpalavra.append(i)

    #correção
    if fixpalavra[idxBitError-1] == 1:
        fixpalavra[idxBitError-1] = '0'
    else:
        fixpalavra[idxBitError-1] == '1'

    
    remolver = size*[0]
    for i in potencias:
        fixpalavra[i-1] = '-'
    
    palavraOriginal = ''
    for i in fixpalavra:
        if (i != '-'):
            palavraOriginal += i

    # toString

    print("\nPalavra Original: ", end="")
    print(palavraOriginal)
    print("\n")

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
