import pymysql.cursors

def index():
    while True:
        print('"Listagem de comandos"')
        print('exit = sair da aplicação')
        print('MD = Mostrar todos os dados da tabela')
        print('ID = Mostra os dados de um ID')
        print('ADD = Inserir novos dados')
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
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='130217',
                             db='crud',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM pessoas")
    result = cursor.fetchall()
    print(result)

def selecioneId(id):
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='130217',
                             db='crud',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM pessoas WHERE id = {id}")
    result = cursor.fetchall()
    print(result)

def inserirDB(nome,email,senha):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='130217',
                                 db='crud',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = f"INSERT INTO pessoas (nome, email, senha) VALUES ('{nome}', '{email}', '{senha}')"
#    print(f'"{sql}"')
    cursor.execute(sql)
    connection.commit()
    connection.close()
