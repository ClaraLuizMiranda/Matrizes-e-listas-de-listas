Leia uma matriz 4 × 4. Calcule e imprima sua transposta. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

matriz = []  
for i in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    matriz.append(linha)

for i in range(4):  
    for j in range(4):  
        print(matriz[j][i],end = " ")    
    print()  
