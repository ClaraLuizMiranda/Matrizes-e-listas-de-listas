Gere uma matriz 5 × 5 com inteiros aleatórios no intervalo [1, 20], encontrados a partir de uma semente dada como entrada. Escreva um programa que transforme a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada. Não use nenhum comando de decisão (se/então/senão).

import random   
matriz = []  
num = int(input("")) 
random.seed(num)     
for i in range(5):  
    linha = []  
    for j in range(5):  
        linha.append(random.randint(1,20))  
    matriz.append(linha) 

for i in range(5):  
    for j in range(5):  
        print(matriz[i][j], end = " ")   
    print()
print() 
incio = 1   
fim = 5
for i in range(5):  
    for j in range(incio):  
        print(matriz[i][j],end = " ")    
    for k in range(fim-incio):  
        print(0,end = " ")  
    incio += 1 
    print()
