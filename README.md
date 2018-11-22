# AOC
# Cógigo de Verificação e Correção de Erros.

Menu:

     Hamming Aplicação

1 - Gerar\
2 - Verificar\ 
0 - Sair\

# Exemplo 1
---------------------------------------------
# 1
Palavra: 11010010\
Nova Palavra: --1-101-0010\
\
Verificação

Bit 1: {1: '-', 3: '1', 5: '1', 7: '1', 9: '0', 11: '1'}\
Bit 2: {2: '-', 3: '1', 6: '0', 7: '1', 10: '0', 11: '1'}\
Bit 4: {4: '-', 5: '1', 6: '0', 7: '1', 12: '0'}\
Bit 8: {8: '-', 9: '0', 10: '0', 11: '1', 12: '0'}\

Contagem de Verificação:\

1: 4\
2: 3\
4: 2\
8: 1\

Impares: [2, 8]\
Nova Palavra: 011010110010\


# Exemplo 2
---------------------------------------------

# 2
Palavra: 110100010100010110000\


Verificação\

Bit 1: {1: '1', 3: '0', 5: '0', 7: '0', 9: '0', 11: '0', 13: '0', 15: '0', 17: '1', 19: '0', 21: '0'}\
Bit 2: {2: '1', 3: '0', 6: '0', 7: '0', 10: '1', 11: '0', 14: '1', 15: '0', 18: '0', 19: '0'}\
Bit 4: {4: '1', 5: '0', 6: '0', 7: '0', 12: '0', 13: '0', 14: '1', 15: '0', 20: '0', 21: '0'}\
Bit 8: {8: '1', 9: '0', 10: '1', 11: '0', 12: '0', 13: '0', 14: '1', 15: '0'}\
Bit 16: {16: '1', 17: '1', 18: '0', 19: '0', 20: '0', 21: '0'}\

Contagem de Verificação:

1: 2\
2: 3\
4: 2\
8: 3\
16: 2\

Impares: [2, 8]\
Candidatos a Erro: [10, 11, 14, 15]\
Bit Errado: 10\

Palavra Original: 0000010001010000\
