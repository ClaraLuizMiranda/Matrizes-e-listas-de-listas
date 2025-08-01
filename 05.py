Leia uma matriz 5 × 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de "Nao encontrado".

matriz = []  
for i in range(5):  
    linha = []  
    for j in range(5):  
        num = int(input("")) 
        linha.append(num)    
    matriz.append(linha) 
num = int(input(""))    
coluna = lin = controle = -1   
for i in range(5):  
    for j in range(5):  
        if matriz[i][j] == num and controle == -1:  
            coluna = j
            lin = i 
            controle = 0
        
if coluna == -1 or lin == -1:    
    print("Nao encontrado") 
else:   
    print(lin)  
    print(coluna)  
