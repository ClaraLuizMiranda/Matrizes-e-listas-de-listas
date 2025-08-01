Leia duas matrizes 4 × 4 e escreva uma terceira matriz com os maiores valores de cada posição das matrizes lidas.


matriz1 = [] 
matriz2 = [] 
matriz3 = [] 

for i in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    matriz1.append(linha)    
for i in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    matriz2.append(linha)    

for i in range(4):  
    linha = []    
    for j in range(4):  
        maior = matriz1[i][j]    
        if matriz2[i][j] > maior:    
            maior = matriz2[i][j]    
        linha.append(maior) 
    matriz3.append(linha)    
        
for i in range(4):  
    for j in range(4):  
        print(matriz3[i][j],end = " ")   
    print()
