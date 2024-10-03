import mysql.connector
from mysql.connector import Error

def conectar_banco():    
    try:
        conexao = mysql.connector.connect(
            host="####",
            user="####",
            database="####",
            password="####"
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida")
            return conexao
            
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None

def consulta(nome):
    conexao = conectar_banco()  

    if conexao is None:
        print("Não foi possível conectar ao banco de dados.")
        return None

    try:
        cursor = conexao.cursor()

        sql = "SELECT nivel_seguranca FROM Funcionarios WHERE nome = %s"
        cursor.execute(sql, (nome,))

        resultado = cursor.fetchone() 

        if resultado:
            return resultado[0]
        else:
            print(f"Nenhum funcionário encontrado com o nome: {nome}")
            return None

    except Error as e:
        print(f'Erro durante a consulta ao MySQL: {e}')
        return None

    finally:
        cursor.close()    
        conexao.close()

