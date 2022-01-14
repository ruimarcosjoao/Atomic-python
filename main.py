import os
from time import sleep
from identificador import identify

while True:
    try:
        print('='*50)
        print('''
        \033[1;33m[0] Organizar todos arquivos\033[m
        \033[1;34m[1] Organizar arquivos por extensao de arquivos\033[m
        \033[1;36m[2] Ajuda e informacao\033[m
        \033[1;31m[3] Sair do programa\033[m
        ''')
        print('='*50)
        sleep(1)
        option = int(input('Escolhe uma opcao: '))
        print()
        if option == 0:
            sleep(1)
            dir_test = input('Escolher diretorio que pretende organizar: ')

            for root, dirs, files in os.walk(dir_test):
                for file in files:
                    src = os.path.join(root, file)
                    identify(file, dir_test, src)
        elif option == 1:

            dir_test = input('Escolher diretorio que pretende organizar: ')
            by_ext = input('Coloca a extensao que pretende organizar: ')

            for root, dirs, files in os.walk(dir_test):
                for file in files:
                    if os.path.isfile(os.path.join(root, file)):
                        if len(os.path.splitext(file)) == 2:
                            name, ext = os.path.splitext(file)
                            if by_ext in ext:
                                src = os.path.join(root, file)
                                identify(file, dir_test, src)
        elif option == 2:
            sleep(1)
            print('''
            Bem vindo/a a ajuda e infomacao
            \033[1;34m[0] info acerca da opcao de organizar todos arquivos
            (a funcao de organizar todos arquivos, consiste em pegar todos arquivos e organizalos
            em suas respetivas pastas. Essa funcao pede a pasta, onde pretendes organizar os arquivos)\033[m
            \033[1;35m[1] info acerca da opcao de organizar arquivos por extensao
            (a funcao de organizar todos arquivos de uma unica funcao, consiste em pegar os arquivos por extensao e organizalos
            em suas respetivas pastas, Essa funcao pede a pasta onde pretendes organizar os arquivos,
            e tambem a extensao do arquivo pretendido)\033[m
            ''')
            sleep(5)

        elif option == 3:
            break
        else:
            print('Escolhe apenas os numeros das opcoes')
    
    except Exception as e:
        print('\033[1;31mColoca apenas numeros que estao nas opcoes dadas.')
        