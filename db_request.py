import mysql.connector
from mysql.connector import Error


def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            database="wayne_db",
            password="7854"
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida")
            return conexao

    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None


def consulta_nivel_seguranca(usuario, senha):
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()

        sql = "SELECT Nivel_seguranca FROM Funcionarios WHERE Usuario = %s AND Senha = %s"
        cursor.execute(sql, (usuario, senha))

        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            print("Usuário e senha não encontrados")
            return None

    except Error as e:
        print(f'Erro durante a consulta ao Banco de Dados: {e}')
        return None

    finally:
        cursor.close()
        conexao.close()


def consulta_inventario():
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()

        sql = "SELECT * FROM Inventario"
        cursor.execute(sql)

        inventario = cursor.fetchall()

        if inventario:
            return inventario
        else:
            print("O inventário está vazio")
            return None

    except Error as e:
        print(f'Erro durante a consulta ao Banco de Dados: {e}')
        return None

    finally:
        cursor.close()
        conexao.close()
