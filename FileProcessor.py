import os
import csv


def main():

    arq = input('Insira o nome do arquivo ')

    name, ext = os.path.splitext(arq)

    if ext == '.txt':
        
        processaTxt(arq)

        
    elif ext == '.csv':

        processaCsv(arq)


    else:

        print('ERRO!')
        

def processaTxt(arq):
    
    with open(arq,'r') as f:
        content = f.read()
        print(content)


def processaCsv(arq):

    with open(arq, newline = '') as f:
        content = csv.reader(f)

        for row in content:
            print(row)


main()
