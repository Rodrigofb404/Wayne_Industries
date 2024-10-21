import mysql.connector
from mysql.connector import Error


def conectar_banco():
    """Estabelece uma conexão com o banco de dados e retorna a conexão."""
    try:
        conexao = mysql.connector.connect(
            host="#########",  # Endereço do servidor do banco de dados
            user="#########",  # Nome de usuário para autenticação
            database="#########",  # Nome do banco de dados a ser utilizado
            password="#########"  # Senha do usuário
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida")
            return conexao  # Retorna a conexão se bem-sucedida

    except Error as e:
        print(f"Erro ao conectar: {e}")  # Exibe erro em caso de falha na conexão
        return None  # Retorna None se a conexão falhar


def consulta_nivel_seguranca(usuario, senha):
    """Consulta o nível de segurança de um usuário com base nas credenciais fornecidas."""
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()
        sql = "SELECT Nivel_seguranca FROM Funcionarios WHERE Usuario = %s AND Senha = %s"
        cursor.execute(sql, (usuario, senha))  # Executa a consulta no banco de dados
        resultado = cursor.fetchone()  # Obtém o resultado da consulta

        if resultado:
            return resultado[0]  # Retorna o nível de segurança se encontrado
        else:
            print("Usuário e senha não encontrados")
            return None  # Retorna None se não encontrar o usuário

    except Error as e:
        print(f'Erro durante a consulta ao Banco de Dados: {e}')
        return None  # Retorna None em caso de erro

    finally:
        cursor.close()  # Fecha o cursor após a operação
        conexao.close()  # Fecha a conexão com o banco de dados


def consulta_inventario():
    """Consulta todos os itens do inventário e retorna a lista de itens."""
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM Inventario"  # SQL para selecionar todos os itens do inventário
        cursor.execute(sql)  # Executa a consulta
        inventario = cursor.fetchall()  # Obtém todos os resultados da consulta

        if inventario:
            return inventario  # Retorna a lista de itens se houver
        else:
            print("O inventário está vazio")
            return None  # Retorna None se o inventário estiver vazio

    except Error as e:
        print(f'Erro durante a consulta ao Banco de Dados: {e}')
        return None  # Retorna None em caso de erro

    finally:
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão


def adicionar_item_inventario(produto, quantidade):
    """Adiciona um novo item ao inventário com a quantidade especificada."""
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()
        sql = "INSERT INTO Inventario (Produto, Quantidade) VALUES (%s, %s)"
        cursor.execute(sql, (produto, quantidade))  # Executa a inserção no banco de dados
        conexao.commit()  # Confirma a inserção
        print(f"Item '{produto}' com quantidade {quantidade} adicionado ao inventário.")

    except Error as e:
        print(f'Erro ao adicionar item ao inventário: {e}')  # Exibe erro em caso de falha na inserção

    finally:
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão


def consulta_funcionarios():
    """Consulta todos os funcionários cadastrados e retorna a lista."""
    conexao = conectar_banco()

    try:
        cursor = conexao.cursor()
        sql = "SELECT * FROM Funcionarios"  # SQL para selecionar todos os funcionários
        cursor.execute(sql)  # Executa a consulta
        inventario = cursor.fetchall()  # Obtém todos os resultados da consulta

        if inventario:
            return inventario  # Retorna a lista de funcionários se houver
        else:
            print("Não há funcionários")
            return None  # Retorna None se não houver funcionários

    except Error as e:
        print(f'Erro durante a consulta ao Banco de Dados: {e}')  # Exibe erro em caso de falha na consulta
        return None  # Retorna None em caso de erro

    finally:
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão


def add_to_inventory(id_produto):
    """Incrementa a quantidade de um item no inventário baseado no ID do produto."""
    conexao = conectar_banco()
    
    try:
        cursor = conexao.cursor()
        sql = """
        UPDATE Inventario
        SET Quantidade = Quantidade + 1
        WHERE id_produto = %s
        """
        cursor.execute(sql, (id_produto,))  # Executa a atualização da quantidade
        conexao.commit()  # Confirma a atualização
        print(f"Quantidade do produto com ID {id_produto} foi incrementada com sucesso.")
        
    except Error as e:
        print(f'Erro: {e}')  # Exibe erro em caso de falha na atualização
        return None

    finally:
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão


def remove_from_inventory(id_produto):
    """Remove ou decrementa a quantidade de um item no inventário baseado no ID do produto."""
    conexao = conectar_banco()
    
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT Quantidade FROM Inventario WHERE id_produto = %s", (id_produto,))
        quantidade_atual = cursor.fetchone()  # Obtém a quantidade atual do produto

        if quantidade_atual:
            quantidade_atual = quantidade_atual[0]  # Extrai a quantidade da tupla

            if quantidade_atual > 1:
                # Decrementa a quantidade se houver mais de um item
                sql = "UPDATE Inventario SET Quantidade = Quantidade - 1 WHERE id_produto = %s"
                cursor.execute(sql, (id_produto,))
                conexao.commit()  # Confirma a atualização
                print(f"Quantidade do produto com ID {id_produto} foi decrementada com sucesso.")
            elif quantidade_atual == 1:
                # Remove o produto se houver apenas um item
                sql = "DELETE FROM Inventario WHERE id_produto = %s"
                cursor.execute(sql, (id_produto,))
                conexao.commit()  # Confirma a remoção
                print(f"Produto com ID {id_produto} foi removido do inventário.")
        else:
            print("Produto não encontrado no inventário.")  # Exibe mensagem se o produto não for encontrado

    except Error as e:
        print(f'Erro: {e}')  # Exibe erro em caso de falha
        return None

    finally:
        cursor.close()  # Fecha o cursor
        conexao.close()  # Fecha a conexão  
