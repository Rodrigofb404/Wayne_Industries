import flet as ft
import db_request as db


def validar_login(usuario: ft.TextField, senha: ft.TextField, page):
    # Valida o login usando as credenciais fornecidas
    nivel_seguranca = db.consulta_nivel_seguranca(usuario.value, senha.value)

    # Redireciona para a página correspondente ao nível de segurança do usuário
    if nivel_seguranca == 1:
        page.go("/areas1")
    elif nivel_seguranca == 2:
        page.go("/areas2")
    elif nivel_seguranca == 3:
        page.go("/areas3")
    else:
        # Exibe uma mensagem de erro se as credenciais estiverem incorretas
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Usuário ou senha incorretos!",
                            color=ft.colors.WHITE),
            bgcolor=ft.colors.RED
        )
        page.snack_bar.open = True  # Abre a barra de notificação
        page.update()


def login_page(page):
    # Configura a página de login
    page.title = "Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_50

    page.controls.clear()  # Limpa os controles existentes na página

    # Adiciona a imagem do logo
    img = ft.Image(
        src="wayne_logo.png",
        width=250,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    titulo = ft.Text("Wayne Industries", size=50, color="Black")

    # Cria campos de entrada para usuário e senha
    usuario = ft.TextField(
        label="Usuário",
        autofocus=True,  # Campo de usuário é focado automaticamente
        width=250,
        border_color=ft.colors.WHITE
    )
    senha = ft.TextField(
        label="Senha",
        password=True,  # Campo é ocultado para senhas
        width=250,
        border_color=ft.colors.WHITE
    )

    # Cria botão de login
    btn = ft.ElevatedButton(
        text="Login",
        width=125,
        on_click=lambda _: validar_login(
            usuario, senha, page)  # Valida login ao clicar
    )

    # Contêiner para agrupar os campos de entrada e botão
    container = ft.Container(
        content=ft.Column(
            controls=[usuario, senha, btn],  # Adiciona campos ao contêiner
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=10,
        bgcolor=ft.colors.BLACK,
        width=500,
        height=300,
        border_radius=10,  # Borda arredondada
        alignment=ft.alignment.center
    )

    # Adiciona todos os componentes à página
    page.add(img, titulo, container)
    page.update()


def nivel1_page(page):
    # Configura a página de áreas restritas nível 1
    page.title = "Áreas Restritas Nível 1 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    # Cria botão para Área Comum
    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            # Redireciona para acesso permitido
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Laboratório
    container_2 = ft.Container(
        content=ft.ElevatedButton(text="Laboratório", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Sala de Controle
    container_3 = ft.Container(
        content=ft.ElevatedButton(text="Sala de Controle", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Cofre
    container_4 = ft.Container(
        content=ft.ElevatedButton(text="Cofre", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Inventário
    container_5 = ft.Container(
        content=ft.ElevatedButton(text="Inventário", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            # Redireciona para a página de inventário
            on_click=lambda _: page.go("/inventario")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Dashboard
    container_dashboard = ft.Container(
        content=ft.ElevatedButton(text="Dashboard", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            # Redireciona para a página do dashboard
            on_click=lambda _: page.go("/dashboard")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Contêiner pai que organiza os botões
    container_pai = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=600,
        height=700,
        content=ft.Column(
            controls=[container_1, container_2, container_3, container_4,
                      container_5, container_dashboard],  # Inclui o dashboard
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border_radius=10,
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()  # Limpa controles anteriores
    page.add(container_pai)  # Adiciona o contêiner pai à página


def nivel2_page(page):
    # Configura a página de áreas restritas nível 2
    page.title = "Áreas Restritas Nível 2 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    # Cria botão para Área Comum
    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Laboratório
    container_2 = ft.Container(
        content=ft.ElevatedButton(text="Laboratório", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Sala de Controle
    container_3 = ft.Container(
        content=ft.ElevatedButton(text="Sala de Controle", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Dashboard
    container_dashboard = ft.Container(
        content=ft.ElevatedButton(text="Dashboard", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/dashboard")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Contêiner pai que organiza os botões
    container_pai = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=600,
        height=600,
        content=ft.Column(
            controls=[container_1, container_2, container_3,
                      container_dashboard],  # Inclui o dashboard
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border_radius=10,
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()  # Limpa controles anteriores
    page.add(container_pai)  # Adiciona o contêiner pai à página


def nivel3_page(page):
    # Configura a página de áreas restritas nível 3
    page.title = "Áreas Restritas Nível 3 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    # Cria botão para Área Comum
    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=100, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Cria botão para Laboratório
    container_2 = ft.Container(
        content=ft.ElevatedButton(text="Laboratório", width=400, height=100, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    # Contêiner pai que organiza os botões
    container_pai = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=600,
        height=600,
        content=ft.Column(
            controls=[container_1, container_2],  # Inclui os botões
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border_radius=10,
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()  # Limpa controles anteriores
    page.add(container_pai)  # Adiciona o contêiner pai à página


def dashboard_page(page: ft.Page):
    normal_radius = 100  # Raio normal dos setores do gráfico
    hover_radius = 130  # Raio dos setores do gráfico quando em hover
    normal_title_style = ft.TextStyle(
        size=18, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD  # Estilo do título normal
    )
    hover_title_style = ft.TextStyle(
        size=24,  # Tamanho do título quando em hover
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        # Sombra para o título em hover
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.BLACK54),
    )

    def on_chart_event(e: ft.PieChartEvent):
        # Atualiza o gráfico ao passar o mouse sobre os setores
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:  # Se o setor estiver sendo destacado
                section.radius = hover_radius  # Altera o raio
                section.title_style = hover_title_style  # Altera o estilo do título
            else:
                section.radius = normal_radius  # Restaura o raio normal
                section.title_style = normal_title_style  # Restaura o estilo normal do título
        chart.update()  # Atualiza o gráfico

    def sair():
        page.go("/")  # Redireciona para a página inicial

    # Consulta a lista de funcionários do banco de dados
    funcionarios = db.consulta_funcionarios()
    niveis_seguranca = {}  # Dicionário para contar funcionários por nível de segurança

    if funcionarios:
        for item in funcionarios:
            nivel = item[4]  # Obtém o nível de segurança do funcionário
            if nivel in niveis_seguranca:
                niveis_seguranca[nivel] += 1  # Incrementa a contagem do nível
            else:
                niveis_seguranca[nivel] = 1  # Inicializa a contagem do nível

    pie_sections = []  # Lista para armazenar as seções do gráfico de pizza

    # Cores para os setores do gráfico
    cores = [ft.colors.RED, ft.colors.GREEN, ft.colors.ORANGE]

    for idx, (nivel, quantidade) in enumerate(niveis_seguranca.items()):
        cor = cores[idx % len(cores)]  # Seleciona a cor para o setor
        pie_sections.append(
            ft.PieChartSection(
                quantidade,
                # Título do setor com a quantidade
                title=f"Nível {nivel}: {quantidade}",
                title_style=normal_title_style,
                color=cor,  # Cor do setor
                radius=normal_radius,  # Raio do setor
            )
        )

    if not pie_sections:  # Se não houver dados para o gráfico
        page.add(
            ft.Text("Nenhum dado disponível para o gráfico.", color=ft.colors.RED))  # Mensagem de aviso
        return  # Sai da função

    chart = ft.PieChart(
        sections=pie_sections,  # Seções do gráfico
        sections_space=5,  # Espaçamento entre os setores
        center_space_radius=40,  # Raio do espaço central do gráfico
        on_chart_event=on_chart_event,  # Evento ao interagir com o gráfico
        expand=True,  # Expande o gráfico para ocupar espaço disponível
    )

    page.title = "Dashboard - Wayne Industries"  # Título da página
    page.bgcolor = ft.colors.WHITE  # Cor de fundo da página
    page.vertical_alignment = ft.MainAxisAlignment.START  # Alinhamento vertical
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal

    page.controls.clear()  # Limpa os controles anteriores da página

    sair_button = ft.ElevatedButton(
        text="Sair",  # Texto do botão
        on_click=lambda e: sair(),  # Função chamada ao clicar
        color=ft.colors.WHITE,
        bgcolor=ft.colors.RED,  # Cor de fundo do botão
        style=ft.ButtonStyle(
            # Estilo arredondado do botão
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    page.add(
        ft.Row(
            controls=[sair_button],  # Adiciona o botão à linha
            alignment=ft.MainAxisAlignment.START,  # Alinhamento da linha
            spacing=10,  # Espaçamento entre os controles
        )
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Dashboard", size=48, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK,
                        text_align=ft.alignment.center),  # Título do dashboard
                chart,  # Gráfico de pizza
                ft.Text(
                    f"Total de Funcionários: {len(funcionarios)}", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)  # Total de funcionários
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento vertical da coluna
            spacing=30,  # Espaçamento entre os controles
            # Alinhamento horizontal da coluna
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.update()  # Atualiza a página


def acesso_permitido_page(page):
    # Configura a página de acesso permitido
    page.title = "Acesso Permitido - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal
    page.bgcolor = ft.colors.BLACK  # Cor de fundo da página

    btn_sair = ft.ElevatedButton(
        text="Sair",  # Texto do botão de sair
        width=100,
        bgcolor=ft.colors.RED,  # Cor de fundo do botão
        color=ft.colors.WHITE,
        on_click=lambda _: page.go("/")  # Redireciona ao clicar
    )

    acesso_text = ft.Text(
        "ACESSO PERMITIDO",  # Texto de acesso permitido
        size=50,
        color=ft.colors.GREEN,  # Cor do texto
        weight=ft.FontWeight.BOLD  # Estilo do texto em negrito
    )

    page.controls.clear()  # Limpa os controles anteriores

    page.add(
        ft.Column(
            [
                ft.Row(
                    [btn_sair],  # Adiciona o botão de sair à linha
                    alignment=ft.MainAxisAlignment.START  # Alinhamento da linha
                ),
                ft.Container(
                    content=acesso_text,  # Adiciona o texto de acesso permitido
                    alignment=ft.alignment.center,  # Alinhamento do texto
                    expand=True  # Expande o contêiner
                )
            ],
            expand=True  # Expande a coluna
        )
    )

    page.update()  # Atualiza a página


def inventario_page(page):
    inventario = db.consulta_inventario()  # Consulta o inventário do banco de dados

    page.title = "Inventário - Wayne Industries"  # Título da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Alinhamento vertical
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Alinhamento horizontal
    page.bgcolor = ft.colors.WHITE  # Cor de fundo da página

    def atualizar_quantidade(id_produto, acao):
        # Atualiza a quantidade de um produto no inventário
        if acao == "add":
            db.add_to_inventory(id_produto)  # Adiciona ao inventário
        elif acao == "remove":
            db.remove_from_inventory(id_produto)  # Remove do inventário
        inventario_page(page)  # Atualiza a página do inventário

    def adicionar_item(e):
        # Adiciona um novo item ao inventário
        produto = input_produto.value  # Obtém o nome do produto
        quantidade = int(input_quantidade.value)  # Obtém a quantidade do produto

        if produto and quantidade > 0:  # Verifica se os dados são válidos
            db.adicionar_item_inventario(produto, quantidade)  # Adiciona item ao banco de dados
            inventario_page(page)  # Atualiza a página do inventário
        else:
            print("Por favor, insira um nome de produto e uma quantidade válida.")  # Mensagem de erro

    if inventario:  # Se houver itens no inventário
        tabela_inventario = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),  # Coluna ID
                ft.DataColumn(ft.Text("Produto", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),  # Coluna Produto
                ft.DataColumn(ft.Text("Quantidade", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),  # Coluna Quantidade
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(
                            str(item[0]), color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),  # ID do produto
                        ft.DataCell(ft.Text(
                            item[1], color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),  # Nome do produto
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.Text(
                                        str(item[2]), color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),  # Quantidade do produto
                                    ft.IconButton(
                                        icon=ft.icons.ADD,  # Botão para adicionar quantidade
                                        icon_color=ft.colors.GREEN,
                                        on_click=lambda e, id_prod=item[0]: atualizar_quantidade(
                                            id_prod, "add")  # Chama função para adicionar
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.REMOVE,  # Botão para remover quantidade
                                        icon_color=ft.colors.RED,
                                        on_click=lambda e, id_prod=item[0]: atualizar_quantidade(
                                            id_prod, "remove")  # Chama função para remover
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER  # Alinhamento dos botões
                            )
                        )
                    ]
                ) for item in inventario  # Itera sobre os itens do inventário
            ],
            width=500,  # Largura da tabela
            column_spacing=10  # Espaçamento entre as colunas
        )
    else:
        tabela_inventario = ft.Text(
            "Inventário vazio.",  # Mensagem quando não há itens no inventário
            size=20,
            color=ft.colors.RED,  # Cor da mensagem
            weight=ft.FontWeight.BOLD  # Estilo em negrito
        )

    input_produto = ft.TextField(
        label="Produto", width=300, color=ft.colors.BLACK)  # Campo para inserir o nome do produto
    input_quantidade = ft.TextField(
        label="Quantidade", width=150, color=ft.colors.BLACK)  # Campo para inserir a quantidade

    btn_adicionar_item = ft.ElevatedButton(
        text="Adicionar Item",  # Texto do botão para adicionar item
        icon=ft.icons.ADD,  # Ícone do botão
        on_click=adicionar_item  # Função chamada ao clicar
    )

    # Botão de Sair
    btn_sair = ft.ElevatedButton(
        text="Sair",  # Texto do botão de sair
        icon=ft.icons.EXIT_TO_APP,  # Ícone do botão de sair
        # Redireciona para a página de login ou inicial
        on_click=lambda _: page.go("/")  # Função chamada ao clicar
    )

    page.controls.clear()  # Limpa os controles anteriores da página
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Inventário", size=40, color=ft.colors.BLACK),  # Título da seção de inventário
                    tabela_inventario,  # Tabela de inventário
                    ft.Divider(height=20, color=ft.colors.GREY),  # Divisória
                    ft.Text("Adicionar novo item ao inventário", size=20, color=ft.colors.BLACK),  # Título da seção de adição
                    ft.Row([input_produto, input_quantidade], spacing=10),  # Linha para campos de entrada
                    btn_adicionar_item,  # Botão para adicionar item
                    btn_sair  # Botão para sair
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento vertical da coluna
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal da coluna
                spacing=20,  # Espaçamento entre os controles
                scroll=ft.ScrollMode.ALWAYS  # Habilita rolagem
            ),
            height=550,  # Altura do contêiner
            width=550  # Largura do contêiner
        )
    )
    page.update()  # Atualiza a página

def main(page: ft.Page):
    def route_change(route):
        # Função para alterar as rotas com base na URL
        if page.route == "/":
            login_page(page)  # Página de login
        elif page.route == "/areas1":
            nivel1_page(page)  # Página de nível 1
        elif page.route == "/areas2":
            nivel2_page(page)  # Página de nível 2
        elif page.route == "/areas3":
            nivel3_page(page)  # Página de nível 3
        elif page.route == "/acesso-permitido":
            acesso_permitido_page(page)  # Página de acesso permitido
        elif page.route == "/inventario":
            inventario_page(page)  # Página do inventário
        elif page.route == "/dashboard":
            dashboard_page(page)  # Página do dashboard

    page.on_route_change = route_change  # Define a função de mudança de rota
    page.go("/")  # Redireciona para a página inicial

ft.app(target=main)  # Inicia o aplicativo
