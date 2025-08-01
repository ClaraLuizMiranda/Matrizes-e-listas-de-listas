Leia uma matriz 4 × 4 , conte e escreva quantos valores maiores que 10 ela possui.

def funcao():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            num = int(input())
            linha.append(num)
        matriz.append(linha)
            
    cont = 0
    for i in range(4):
        for j in range(4):
            if matriz[i][j] > 10:
                cont += 1
                
    print(cont)

funcao()
