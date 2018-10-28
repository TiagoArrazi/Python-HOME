def main():

    print('INSIRA AS DIMENSÕES DA 1ª MATRIZ \n')

    L1 = int(input('Número de linhas '))
    C1 = int(input('Número de colunas '))

    M1 = []

    for i in range(L1):
        M1.append([])

        for j in range(C1):
            M1[i].append(int(input('Insira o valor na posição ' +
                               '(' + str(i + 1) + ' ; ' +
                               str(j + 1) + ')' + ' ')))

    print(M1)
    print('\n')

    print('INSIRA AS DIMENSÕES DA 2ª MATRIZ \n')

    L2 = int(input('Número de linhas '))
    C2 = int(input('Número de colunas '))

    M2 = []

    for i in range(L2):
        M2.append([])

        for j in range(C2):
            M2[i].append(int(input('Insira o valor na posição ' +
                               '(' + str(i + 1) + ' ; ' +
                               str(j + 1) + ')' + ' ')))

    print(M2)
    print('\n')

    MatrixMult(M1,L1,C1,M2,L2,C2)

def MatrixMult(M1,L1,C1,M2,L2,C2):

    if C1 != L2:
        
        print('MATRIZES INCOMPATÍVEIS!')
        return -1

    else:
        
        M3 = [[sum(i*j for i,j in zip(L1,C2))
               for C2 in zip(*M2)]
              for L1 in M1]
        
        for m in M3:
            print(m)


main()
