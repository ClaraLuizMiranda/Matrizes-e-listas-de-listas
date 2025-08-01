Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada linha pelo maior elemento em módulo daquela linha. Escreva a matriz original e a modificada.

A = []  
for i in range(12): 
    linha = []  
    for j in range(13): 
        linha.append(int(input("")))    
    A.append(linha) 

for i in range(12): 
    for j in range(13): 
        print(f"{A[i][j]:.2f}",end = " ")    
    print() 
print()
B = []
for i in range(12): 
    maior = 0    
    linha = []   
    for j in range(13): 
         
        if A[i][j] < 0: 
            if A[i][j]*-1 > maior:  
                maior = A[i][j]*-1  
        if A[i][j] > maior: 
            maior = A[i][j] 
    for k in range(13): 
        linha.append(A[i][k]/maior)
    B.append(linha)

for i in range(12): 
    for j in range(13): 
        print(f"{B[i][j]:.2f}",end = " ") 
    print()
