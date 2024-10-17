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

def add_to_inventory(id_produto):
    conexao = conectar_banco()
    
    try:
        cursor = conexao.cursor()

        sql = """
        UPDATE Inventario
        SET Quantidade = Quantidade + 1
        WHERE id_produto = %s
        """
        cursor.execute(sql, (id_produto,))

        # Confirma a transação
        conexao.commit()
        print(f"Quantidade do produto com ID {id_produto} foi incrementada com sucesso.")
        
    except Error as e:
        print(f'Erro: {e}')
        return None

    finally:
        cursor.close()
        conexao.close()

def remove_from_inventory(id_produto):
    conexao = conectar_banco()
    
    try:
        cursor = conexao.cursor()

        sql = """
        UPDATE Inventario
        SET Quantidade = Quantidade - 1
        WHERE id_produto = %s
        """
        cursor.execute(sql, (id_produto,))

        conexao.commit()
        print(f"Quantidade do produto com ID {id_produto} foi decrementada com sucesso.")
        
    except Error as e:
        print(f'Erro: {e}')
        return None

    finally:
        cursor.close()
        conexao.close()