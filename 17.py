Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada coluna pelo maior elemento daquela coluna que seja primo. Caso a coluna não possua um número primo, divida a coluna pelo menor número da coluna. Escreva a matriz original e a modificada.

def imprimir_matriz(Matriz):
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            print(f"{Matriz[i][j]:.2f} ", end="")
        print("")
def inicializador(linha, coluna):
    Matriz = []
    for i in range(linha):
        Matriz.append([])
        for j in range(coluna):
            Matriz[i].append(0)
    return Matriz
Matriz12x13 = []
for i in range(12):
    Matriz12x13.append([])
    for j in range(13):
        Matriz12x13[i].append(int(input()))
Matriz_dividida = inicializador(12, 13)
for i in range(13):
    verificacao = True
    maior_encontrado = False
    maior = -999
    menor = 0
    for j in range(12):
        if verificacao:
            for k in range(12):
                cont = 0
                e_primo = False
                for l in range(1, abs(Matriz12x13[k][i])+1):
                    if abs(Matriz12x13[k][i]) % l == 0:
                        cont += 1
                    if cont > 2:
                        break
                    elif l == abs(Matriz12x13[k][i]) and cont <= 2:
                        e_primo = True
                if e_primo and Matriz12x13[k][i] > maior:
                    maior = Matriz12x13[k][i]
                    maior_encontrado = True
                elif Matriz12x13[k][i] < menor:
                    menor = Matriz12x13[k][i]
            verificacao = False
        if maior_encontrado:
            Matriz_dividida[j][i] = round(Matriz12x13[j][i] / maior, 2)
        else:
            Matriz_dividida[j][i] = round(Matriz12x13[j][i] / menor, 2)
imprimir_matriz(Matriz12x13)
print("")
imprimir_matriz(Matriz_dividida)
