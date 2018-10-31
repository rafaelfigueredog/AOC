# AOC
# Códigos de correção de erros

  Erros em memórias
    Picos de tensão
    Raios cósmicos
    
# Distância de Hamming
  Número de posições de bit que diferem entre duas palavras
  Contagem de bits 1 após XOR entre duas palavras
  Exemplos
    Hamming(11110001, 00110000) = 3
    Hamming(11011, 10011) = 1
    Hamming(1010101, 0110011) = 4

# Redundância
  Palavra de m bits
  Detector/corretor de r bits
  Palavra de código de n bits (n = m + r)
  Redundância R = n / m
# Detecção de erro único
  Bit de paridade
  Indica se quantidade de bits 1 é par ou ímpar
  R = n / (n - 1)
  Exemplo
    01110001 = 0 (par) 1110001 (4)
    11011101 = 1 (ímpar) 1011101 (5)

# Correção de erro
  Distância = 2d + 1
  d é quantidade de erros
  Error Detecting and Error Correcting Codes (HAMMING, 1950)
  Exemplo
    Palavras válidas: 0000000000, 0000011111, 1111100000 e 1111111111
    Distância mínima = 5
    Quantidade de erros
    Distância = 2d + 1
      5 = 2d + 1
      2d = 5 - 1
      2d = 4
      d = 2


# Limitações
    Projeto de código para m bits de dados e r bits de verificação
    Quantidade de palavras válidas = 2m
    Para cada palavra válida, n palavras inválidas
    Obtidas invertendo cada bit de cada vez
    Total de padrões associado a cada palavra válida = n + 1
    Soma das palavras inválidas com a válida
    Condição
      2m (n + 1) ≤ 2n
      2m (m + r + 1) ≤ 2m + r
      2m (m + r + 1) ≤ 2m . 2r
      2m (m + r + 1) ≤ 2m . 2r
      m + r + 1 ≤ 2r
      Dado m, é possível estabelecer r mínimo
      Linear x exponencial
