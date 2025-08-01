Faça um programa que preenche uma matriz de tamanho nxn com o produto do valor da linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz, em forma de tabela.

n = int(input())
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(i*j)
    matriz.append(linha)
    
for i in range(n):
    for j in range(n):
        print(matriz[i][j],end = " ")
    print()    
