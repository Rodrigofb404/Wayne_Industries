# Sistema de Controle de Acesso - Wayne Industries

Este projeto implementa uma interface para controle de acesso às áreas restritas das Indústrias Wayne. O sistema valida as credenciais de login, direciona os usuários para diferentes áreas de acesso com base em seu nível de segurança e também inclui uma interface para a gestão do inventário.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flet**: Framework para construção da interface gráfica.
- **MySQL**: Banco de dados relacional utilizado para armazenar informações de funcionários e inventário.

## Funcionalidades

- **Autenticação de Usuário**: Com base em login e senha, os usuários são redirecionados para diferentes áreas conforme seu nível de segurança.
- **Níveis de Segurança**:
  - Nível 1: Acesso a todas as áreas.
  - Nível 2: Acesso limitado.
  - Nível 3: Acesso mais restrito.
- **Gestão de Inventário**: Consulta, atualização, adição e remoção de itens de inventário.
- **Dashboard**: Gráfico de distribuição dos funcionários por nível de segurança.
- **Página de Acesso Permitido**: Confirmação de que o usuário tem o nível de segurança necessário para acessar a área.

## Estrutura do Projeto

- **interface.py**: Arquivo principal contendo a lógica da interface gráfica e navegação entre as páginas.
- **db_request.py**: Contém funções que fazem a comunicação com o banco de dados MySQL, como consultas e atualizações.

---

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/usuario/projeto-controle-acesso.git
cd projeto-controle-acesso
```  

### 2. Instalar Bibliotecas

```bash
pip install flet
pip install mysql-connector-python
```

### 3. Configurar Banco de Dados

Crie o banco de dados MySQL e as tabelas conforme a estrutura abaixo:
```bash
CREATE TABLE Funcionário (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Salário DECIMAL(10, 2) NOT NULL,
    Cargo ENUM('Diretor', 'Adm_Seguranca', 'Gerente') NOT NULL,
    Nivel_seguranca INT NOT NULL,
    Usuario VARCHAR(50) NOT NULL UNIQUE,
    Senha VARCHAR(255) NOT NULL
);
```

```bash
CREATE TABLE Inventario (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    Produto VARCHAR(100),
    Quantidade INT
);
```
Após criar as tabelas, insira os dados.  
**OBS:** Os dados da tabela funcionários só podem ser inserido diretamente pelo MySQL.

### 4. Configurar Conexão Com o Banco de Dados

No arquivo `db_request.py`, substitua as variáveis de conexão com o banco de dados:

```bash
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host="SEU_HOST",
            user="SEU_USUARIO",
            database="NOME_DO_BANCO",
            password="SUA_SENHA"
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None
```

### 5. Executar Aplicação

Após configurar o banco de dados e as bibliotecas, execute o arquivo principal:
```bash
interface.py
```
