import flet as ft
import db_request as db


def validar_login(usuario: ft.TextField, senha: ft.TextField, page):
    # Valida o login
    nivel_seguranca = db.consulta_nivel_seguranca(usuario.value, senha.value)

    if nivel_seguranca == 1:
        page.go("/areas1")
    elif nivel_seguranca == 2:
        page.go("/areas2")
    elif nivel_seguranca == 3:
        page.go("/areas3")
    else:
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Usuário ou senha incorretos!",
                            color=ft.colors.WHITE),
            bgcolor=ft.colors.RED
        )
        page.snack_bar.open = True
        page.update()


def login_page(page):
    page.title = "Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_50

    page.controls.clear()

    img = ft.Image(
        src="wayne_logo.png",
        width=250,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    titulo = ft.Text("Wayne Industries", size=50, color="Black")

    usuario = ft.TextField(
        label="Usuário",
        autofocus=True,
        width=250,
        border_color=ft.colors.WHITE
    )
    senha = ft.TextField(
        label="Senha",
        password=True,
        width=250,
        border_color=ft.colors.WHITE
    )

    btn = ft.ElevatedButton(
        text="Login",
        width=125,
        on_click=lambda _: validar_login(usuario, senha, page)
    )

    container = ft.Container(
        content=ft.Column(
            controls=[usuario, senha, btn],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        margin=10,
        padding=10,
        bgcolor=ft.colors.BLACK,
        width=500,
        height=300,
        border_radius=10,
        alignment=ft.alignment.center
    )

    page.add(img, titulo, container)
    page.update()


def nivel1_page(page):
    page.title = "Áreas Restritas Nível 1 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_2 = ft.Container(
        content=ft.ElevatedButton(text="Laboratório", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_3 = ft.Container(
        content=ft.ElevatedButton(text="Sala de Controle", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_4 = ft.Container(
        content=ft.ElevatedButton(text="Cofre", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_200, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_5 = ft.Container(
        content=ft.ElevatedButton(text="Inventário", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/inventario")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_dashboard = ft.Container(
        content=ft.ElevatedButton(text="Dashboard", width=400, height=70, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/dashboard")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

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

    page.controls.clear()
    page.add(container_pai)


def nivel2_page(page):
    page.title = "Áreas Restritas Nível 2 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_2 = ft.Container(
        content=ft.ElevatedButton(text="Laboratório", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_3 = ft.Container(
        content=ft.ElevatedButton(text="Sala de Controle", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_dashboard = ft.Container(
        content=ft.ElevatedButton(text="Dashboard", width=400, height=80, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/dashboard")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_pai = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=600,
        height=600,
        content=ft.Column(
            controls=[container_1, container_2, container_3,
                      container_dashboard], 
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border_radius=10,
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()
    page.add(container_pai)


def nivel3_page(page):
    page.title = "Áreas Restritas Nível 3 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=100, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_2 = ft.Container(
        content=ft.ElevatedButton(text="Laboratório", width=400, height=100, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_pai = ft.Container(
        bgcolor=ft.colors.BLACK,
        width=600,
        height=600,
        content=ft.Column(
            controls=[container_1, container_2],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        border_radius=10,
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()
    page.add(container_pai)


def dashboard_page(page: ft.Page):
    normal_radius = 100
    hover_radius = 130
    normal_title_style = ft.TextStyle(
        size=18, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
    )
    hover_title_style = ft.TextStyle(
        size=24,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        shadow=ft.BoxShadow(blur_radius=4, color=ft.colors.BLACK54),
    )

    def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        chart.update()

    def sair():
        page.go("/")  

    funcionarios = db.consulta_funcionarios()
    niveis_seguranca = {}

    if funcionarios:
        for item in funcionarios:
            nivel = item[4]  
            if nivel in niveis_seguranca:
                niveis_seguranca[nivel] += 1
            else:
                niveis_seguranca[nivel] = 1

    pie_sections = []

    cores = [ft.colors.RED, ft.colors.GREEN,
             ft.colors.ORANGE]

    for idx, (nivel, quantidade) in enumerate(niveis_seguranca.items()):
        cor = cores[idx % len(cores)]
        pie_sections.append(
            ft.PieChartSection(
                quantidade,
                title=f"Nível {nivel}: {quantidade}",
                title_style=normal_title_style,
                color=cor, 
                radius=normal_radius,
            )
        )

    if not pie_sections:
        page.add(
            ft.Text("Nenhum dado disponível para o gráfico.", color=ft.colors.RED))
        return 

    chart = ft.PieChart(
        sections=pie_sections,
        sections_space=5, 
        center_space_radius=40,
        on_chart_event=on_chart_event,
        expand=True,
    )

    page.title = "Dashboard - Wayne Industries"
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.START 
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.controls.clear()

    sair_button = ft.ElevatedButton(
        text="Sair",
        on_click=lambda e: sair(),
        color=ft.colors.WHITE,
        bgcolor=ft.colors.RED,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )

    page.add(
        ft.Row(
            controls=[sair_button],
            alignment=ft.MainAxisAlignment.START,
            spacing=10,  
        )
    )

    page.add(
        ft.Column(
            controls=[
                ft.Text("Dashboard", size=48, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK,
                        text_align=ft.alignment.center), 
                chart,
                ft.Text(
                    f"Total de Funcionários: {len(funcionarios)}", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=30, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
        )
    )
    page.update()





def acesso_permitido_page(page):
    page.title = "Acesso Permitido - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    btn_sair = ft.ElevatedButton(
        text="Sair",
        width=100,
        bgcolor=ft.colors.RED,
        color=ft.colors.WHITE,
        on_click=lambda _: page.go("/")  
    )

    acesso_text = ft.Text(
        "ACESSO PERMITIDO",
        size=50,
        color=ft.colors.GREEN,
        weight=ft.FontWeight.BOLD
    )

    page.controls.clear()

    page.add(
        ft.Column(
            [
                ft.Row(
                    [btn_sair],
                    alignment=ft.MainAxisAlignment.START  
                ),
                ft.Container(
                    content=acesso_text,
                    alignment=ft.alignment.center,
                    expand=True 
                )
            ],
            expand=True
        )
    )

    page.update()


def inventario_page(page):
    inventario = db.consulta_inventario()

    page.title = "Inventário - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    def atualizar_quantidade(id_produto, acao):
        if acao == "add":
            db.add_to_inventory(id_produto)
        elif acao == "remove":
            db.remove_from_inventory(id_produto)
        inventario_page(page)

    def adicionar_item(e):
        produto = input_produto.value
        quantidade = int(input_quantidade.value)

        if produto and quantidade > 0:
            db.adicionar_item_inventario(produto, quantidade)
            inventario_page(page)
        else:
            print("Por favor, insira um nome de produto e uma quantidade válida.")

    if inventario:
        tabela_inventario = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),
                ft.DataColumn(ft.Text("Produto", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),
                ft.DataColumn(ft.Text("Quantidade", color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(item[0]), color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),  # ID
                        ft.DataCell(ft.Text(item[1], color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER)),        # Produto
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.Text(str(item[2]), color=ft.colors.BLACK, text_align=ft.TextAlign.CENTER),
                                    ft.IconButton(
                                        icon=ft.icons.ADD,
                                        icon_color=ft.colors.GREEN,
                                        on_click=lambda e, id_prod=item[0]: atualizar_quantidade(id_prod, "add")  # Incrementar
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.REMOVE,
                                        icon_color=ft.colors.RED,
                                        on_click=lambda e, id_prod=item[0]: atualizar_quantidade(id_prod, "remove")  # Decrementar
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            )
                        )
                    ]
                ) for item in inventario
            ],
            width=500,
            column_spacing=10
        )
    else:
        tabela_inventario = ft.Text(
            "Inventário vazio.",
            size=20,
            color=ft.colors.RED,
            weight=ft.FontWeight.BOLD
        )

    input_produto = ft.TextField(label="Produto", width=300, color=ft.colors.BLACK)
    input_quantidade = ft.TextField(label="Quantidade", width=150, color=ft.colors.BLACK)

    btn_adicionar_item = ft.ElevatedButton(
        text="Adicionar Item",
        icon=ft.icons.ADD,
        on_click=adicionar_item
    )

    # Botão de Sair
    btn_sair = ft.ElevatedButton(
        text="Sair",
        icon=ft.icons.EXIT_TO_APP,
        on_click=lambda _: page.go("/")  # Redireciona para a página de login ou inicial
    )

    page.controls.clear()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Inventário", size=40, color=ft.colors.BLACK),
                    tabela_inventario,
                    ft.Divider(height=20, color=ft.colors.GREY),
                    ft.Text("Adicionar novo item ao inventário", size=20, color=ft.colors.BLACK),
                    ft.Row([input_produto, input_quantidade], spacing=10),
                    btn_adicionar_item,
                    btn_sair
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.ALWAYS
            ),
            height=550,
            width=550
        )
    )
    page.update()



def main(page: ft.Page):
    def route_change(route):
        if page.route == "/":
            login_page(page)
        elif page.route == "/areas1":
            nivel1_page(page)
        elif page.route == "/areas2":
            nivel2_page(page)
        elif page.route == "/areas3":
            nivel3_page(page)
        elif page.route == "/acesso-permitido":
            acesso_permitido_page(page)
        elif page.route == "/inventario":
            inventario_page(page)
        elif page.route == "/dashboard":
            dashboard_page(page)

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)
