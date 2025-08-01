Faça um programa que gere uma matriz m × n de inteiros aleatórios (gerados a partir de uma semente), calcule e mostre a média dos elementos das linhas pares da matriz e a quantidade de números negativos e divisíveis por 3 das linhas ímpares da matriz. A quantidade de linhas m, a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão dados como entrada para o programa.

import random   
matriz = []
m = int(input(""))  
n = int(input(""))  
semente = int(input("")) 
random.seed(semente)    
inicio = int(input("")) 
fim = int(input(""))    
for i in range(m):  
    linha = []  
    for j in range(n):  
        linha.append(random.randint(inicio,fim))    
    matriz.append(linha) 

for i in range(m):   
    for j in range(n):  
        print(matriz[i][j], end = " ")         
    print() 
par = 0   
contador = 0    
impar = 0 

for i in range(m):  
    par = 0   
    contador = 0    
    impar = 0  
    for j in range(n):  
        if i%2 == 0:    
            par += matriz[i][j]    
            contador += 1   
        if i%2 == 1 and matriz[i][j] < 0 and matriz[i][j]%3 == 0:    
            impar += 1  
    if contador != 0:   
        print(f"{par/contador:.2f}")   
    if i%2 == 1:   
        print(f"{impar}")
