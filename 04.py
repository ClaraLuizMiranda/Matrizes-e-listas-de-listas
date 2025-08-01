Leia uma matriz 4 × 4, imprima a matriz e retorne a localização (linha e coluna) do maior valor.

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        num = int(input("")) 
        linha.append(num)    
    matriz.append(linha)    

maior = mlin = mcol = 0 
for i in range(4):  
    if i == 0:  
        maior = matriz[i][0]    
    for j in range(4):  
        if matriz[i][j] > maior:    
            maior = matriz[i][j]    
            mlin = i    
            mcol = j    
        print(f"{matriz[i][j]}", end = " ")    
    print() 
print(mlin) 
print(mcol) 
print(maior)
      
