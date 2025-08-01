Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão na diagonal secundária. Use apenas um comando de repetição. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.

matriz = []  
for i in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    matriz.append(linha) 
     
diagonal = 3    
soma = 0
for i in range(4):  
    for j in range(4):  
        if j == diagonal:     
            diagonal -= 1   
            soma += matriz[i][j]  
print(soma)  
