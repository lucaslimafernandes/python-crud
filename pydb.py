import pymysql.cursors

def conn():
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
#
