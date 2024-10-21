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
## Detalhamento do Código

### interface.py

Este arquivo contém toda a lógica da interface do sistema, desde o login até a navegação entre as páginas com base no nível de segurança do usuário.

#### Funções Principais

- **`validar_login(usuario: ft.TextField, senha: ft.TextField, page)`**:
  - **Descrição**: Valida o login do usuário com base nas credenciais inseridas (usuário e senha) e redireciona para a página apropriada de acordo com o nível de segurança.
  - **Parâmetros**:
    - `usuario`: Campo de texto que contém o nome do usuário.
    - `senha`: Campo de texto que contém a senha do usuário.
    - `page`: Objeto da página atual, utilizado para navegação.
  - **Fluxo**:
    1. Obtém o nível de segurança chamando `db.consulta_nivel_seguranca(usuario.value, senha.value)`.
    2. Compara o nível de segurança obtido:
       - Se `nivel_seguranca == 1`, redireciona para a página de Nível 1.
       - Se `nivel_seguranca == 2`, redireciona para a página de Nível 2.
       - Se `nivel_seguranca == 3`, redireciona para a página de Nível 3.
    3. Caso as credenciais estejam incorretas, exibe uma mensagem de erro.

- **`login_page(page)`**:
  - **Descrição**: Exibe a página de login com campos de Usuário e Senha.
  - **Parâmetros**:
    - `page`: Objeto da página atual.
  - **Fluxo**:
    1. Define o título e a cor de fundo da página.
    2. Limpa quaisquer controles existentes na página.
    3. Adiciona a logo da empresa e o título.
    4. Cria campos de entrada para usuário e senha, com estilos personalizados.
    5. Cria um botão de login que chama a função `validar_login()` ao ser clicado.
    6. Organiza os elementos da página em um contêiner e os adiciona à página.

- **`nivel1_page(page)`**, **`nivel2_page(page)`**, **`nivel3_page(page)`**:
  - **Descrição**: Exibem as áreas acessíveis para cada nível de segurança (Nível 1, Nível 2 e Nível 3).
  - **Parâmetros**:
    - `page`: Objeto da página atual.
  - **Fluxo Comum**:
    1. Define o título da página e as cores de fundo.
    2. Cria botões para as áreas acessíveis, cada um com um texto e um estilo personalizado.
    3. Cada botão é vinculado a uma ação de navegação que redireciona o usuário para uma página de acesso permitido ou outras funcionalidades.
    4. Organiza todos os botões em um contêiner pai e o adiciona à página.

- **`inventario_page(page)`**:
  - **Descrição**: Mostra a página do inventário, permitindo a visualização, atualização, adição e remoção de itens (para deletar o item remova até `Quantidade = 0`).
  - **Parâmetros**:
    - `page`: Objeto da página atual.
  - **Fluxo**:
    1. Define o título e a cor de fundo da página.
    2. Recupera itens do inventário usando `db.consulta_inventario()`.
    3. Exibe os itens em uma tabela com opções para adicionar, remover e modificar itens.

- **`dashboard_page(page)`**:
  - **Descrição**: Exibe um gráfico de pizza com a distribuição dos funcionários por nível de segurança.
  - **Parâmetros**:
    - `page`: Objeto da página atual.
  - **Fluxo**:
    1. Define o título e a cor de fundo da página.
    2. Obtém dados sobre a distribuição dos funcionários do banco de dados.
    3. Cria e exibe um gráfico de pizza baseado nos dados obtidos.

- **`acesso_permitido_page(page)`**:
  - **Descrição**: Página de confirmação quando o usuário tem acesso permitido.
  - **Parâmetros**:
    - `page`: Objeto da página atual.
  - **Fluxo**:
    1. Adiciona um texto confirmando que o acesso foi permitido.

---

### db_request.py

Este arquivo contém funções responsáveis por conectar e realizar operações no banco de dados MySQL.

#### Funções Principais

- **`conectar_banco()`**:
  - **Descrição**: Realiza a conexão com o banco de dados.
  - **Fluxo**:
    1. Cria uma conexão utilizando as credenciais do banco de dados.
    2. Caso o comando seja bem sucedido, retorna a conexão para uso em outras funções.

- **`consulta_nivel_seguranca(usuario: str, senha: str)`**:
  - **Descrição**: Consulta o nível de segurança do funcionário no banco com base nas credenciais inseridas.
  - **Parâmetros**:
    - `usuario`: Nome do usuário para autenticação.
    - `senha`: Senha do usuário para autenticação.
  - **Fluxo**:
    1. Executa uma consulta SQL para verificar as credenciais.
    2. Caso o comando seja bem sucedido, retorna o nível de segurança correspondente.

- **`consulta_inventario()`**:
  - **Descrição**: Retorna todos os itens do inventário.
  - **Fluxo**:
    1. Executa uma consulta SQL para obter todos os itens.
    2. Caso o comando seja bem sucedido, retorna os itens em uma lista de tuplas.

- **`adicionar_item_inventario(produto, quantidade)`**:
  - **Descrição**: Adiciona um novo item ao inventário.
  - **Parâmetros**:
    - `produto`: String contendo o nome do produto a ser adicionado.
    - `quantidade`: inteiro contendo a quantidade que será adicionada.
  - **Fluxo**:
    1. Executa uma consulta SQL para inserir o item no inventário.
    2. Caso o comando seja bem sucedido, realiza a adição do item ao inventário.

- **`consulta_funcionarios()`**:
  - **Descrição**: Retorna todos os funcionários cadastrados no banco.
  - **Fluxo**:
    1. Executa uma consulta SQL para obter a lista de funcionários.
    2. Caso o comando seja bem sucedido, retorna os dados dos funcionários em uma lista de tuplas.
  
- **`add_to_inventory(id_produto)`**:
  - **Descrição**: Incrementa a quantidade de um produto no inventário.
  - **Parâmetro**:
    - `id_produto`: Inteiro que representa o ID do produto a ser atualizado.
  - **Fluxo**:
    1. Executa uma consulta SQL para inserir o item no inventário.
    2. Caso o comando seja bem sucedido, incrementa a quantidade do produto correspondente com 1.

- **`remove_from_inventory(id_produto)`**:
  - **Descrição**: Decrementa a quantidade de um produto no inventário ou remove o produto caso a quantidade chegue a zero.
  - **Parâmetro**:
    - `id_produto`: Inteiro que representa o ID do produto a ser removido ou decrementado.
  - **Fluxo**:
    1. Executa uma consulta SQL para inserir o item no inventário.
    2. Caso o comando seja bem sucedido e `Quantidade > 1`, decrementa a quantidade do produto correspondente com 1. Caso `Quantidade = 1`, deleta o produto da tabela.

---

### Fluxo da Aplicação

1. O usuário acessa a Página de Login.
2. Dependendo das credenciais fornecidas, o sistema redireciona o usuário para a página correspondente ao seu nível de segurança;
3. O usuário com **Nível de Segurança 1 ou 2** pode acessar o inventário e o dashboard:
   - **Inventário**: O usuário pode consultar, atualizar, adicionar e remover itens do inventário.
   - **Dashboard**: O usuário visualiza um gráfico da distribuição de funcionários por nível de segurança.
4. O botão "Sair" retorna o usuário para a página de login, permitindo que outro usuário faça login no sistema.

---
