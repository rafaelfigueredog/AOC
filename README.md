# Organização e Arquiterura de Computadores IFPB
## Código de Verificação e Correção de Erros.
##### Rafael Figueredo Guimarães <br />

###### Primeira Impressão<br />

Menu:

<p>    Hamming Aplicação

1 - Gerar <br />
2 - Verificar <br />
0 - Sair <br />
</p>

### Exemplo 1
---------------------------------------------
###### # 1
Palavra: 11010010 <br />
Nova Palavra: --1-101-0010 <br />
<br />
Verificação<br />
<br />
Bit 1: {1: '-', 3: '1', 5: '1', 7: '1', 9: '0', 11: '1'} <br />
Bit 2: {2: '-', 3: '1', 6: '0', 7: '1', 10: '0', 11: '1'} <br />
Bit 4: {4: '-', 5: '1', 6: '0', 7: '1', 12: '0'} <br />
Bit 8: {8: '-', 9: '0', 10: '0', 11: '1', 12: '0'} <br />

Contagem de Verificação:<br />
<br />
1: 4 <br />
2: 3 <br />
4: 2 <br />
8: 1 <br />
<br />
Impares: [2, 8] <br />
Nova Palavra: 011010110010 <br />
<br />
### Exemplo 2
---------------------------------------------
###### # 2
Palavra: 110100010100010110000<br />

Verificação<br />

Bit 1: {1: '1', 3: '0', 5: '0', 7: '0', 9: '0', 11: '0', 13: '0', 15: '0', 17: '1', 19: '0', 21: '0'}<br />
Bit 2: {2: '1', 3: '0', 6: '0', 7: '0', 10: '1', 11: '0', 14: '1', 15: '0', 18: '0', 19: '0'}<br />
Bit 4: {4: '1', 5: '0', 6: '0', 7: '0', 12: '0', 13: '0', 14: '1', 15: '0', 20: '0', 21: '0'}<br />
Bit 8: {8: '1', 9: '0', 10: '1', 11: '0', 12: '0', 13: '0', 14: '1', 15: '0'}<br />
Bit 16: {16: '1', 17: '1', 18: '0', 19: '0', 20: '0', 21: '0'}<br />
<br />
Contagem de Verificação:<br />
<br />
1: 2<br />
2: 3<br />
4: 2<br />
8: 3<br />
16: 2<br />

Impares: [2, 8]<br />
Candidatos a Erro: [10, 11, 14, 15]<br />
Bit Errado: 10<br />

Palavra Original: 0000010001010000<br />
