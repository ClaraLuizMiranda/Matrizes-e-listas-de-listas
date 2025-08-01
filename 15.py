Faça um programa que leia duas matrizes A e B de tamanho 5 × 5 cada uma. Calcule a matriz C = A * B. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

A = []  
for i in range(5):  
    linha = []
    for j in range(5):  
        linha.append(int(input("")))    
    A.append(linha) 

B = []  
for i in range(5):  
    linha = []
    for j in range(5):  
        linha.append(int(input("")))    
    B.append(linha) 

C = []            
for i in range(5):
    linha = []
    for j in range(5):
        elemento = 0
        for k in range(5):
            elemento += A[i][k] * B[k][j]
        linha.append(elemento)
    C.append(linha)

for i in range(5):  
    for j in range(5):  
        print(C[i][j],end = " ")    
    print()
