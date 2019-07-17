import pymysql.cursors

connection = pymysql.connect(host='localhost',
                        user='root',
                        password='130217',
                        db='crud',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()


def index():
    while True:
        print('-'*40)
        print('"Listagem de comandos"')
        print('exit = sair da aplicação')
        print('MD = Mostrar todos os dados da tabela')
        print('ID = Mostra os dados de um ID')
        print('ADD = Inserir novos dados')
        print('-'*40)
        cmd = str(input('Digite o comando desejado: ')).strip().lower()
        if cmd =='exit':
            break
        elif cmd =='md':
            mostrarDados()
        elif cmd =='id':
            a = int(input('Digite o ID que deseja ver: '))
            selecioneId(a)
        elif cmd =='add':
            nome = str(input('Digite o nome: '))
            email = str(input('Digite o e-mail: '))
            senha = str(input('Digite a senha: '))
            inserirDB(nome, email, senha)


def mostrarDados():
    cursor.execute("SELECT * FROM pessoas")
    result = cursor.fetchall()
    resultChaves = result[0]
    for k, v in resultChaves.items():
        print(k, end='  ')
    print()

def selecioneId(id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM pessoas WHERE id = {id}")
    result = cursor.fetchall()
    print(result)

def inserirDB(nome,email,senha):
    cursor = connection.cursor()
    sql = f"INSERT INTO pessoas (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')"
    cursor.execute(sql)
    connection.commit()
    connection.close()


#https://pt.stackoverflow.com/questions/308346/como-imprimir-as-informa%C3%A7%C3%B5es-no-formato-de-tabela-em-python
