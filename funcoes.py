from pydb import *

def index():
    while True:
        print('"Listagem de comandos"')
        print('exit = sair da aplicação')
        print('MD = Mostrar todos os dados da tabela')
        cmd = str(input('Digite o comando desejado: ')).strip().lower()
        if cmd =='exit':
            break
        elif cmd =='md':
            mostrarDados()



def mostrarDados():
    conn()
