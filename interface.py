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
            content=ft.Text("Usuário ou senha incorretos!", color=ft.colors.WHITE),
            bgcolor=ft.colors.RED
        )
        page.snack_bar.open = True
        page.update()

def login_page(page):
    page.title = "Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_50

    img = ft.Image(
        src="wayne_logo.png",
        width=250,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    titulo = ft.Text("Wayne Industries", size=50, color="Black")

    # Campos de texto para entrada do usuário e senha
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

    # Botão de login que chama a função de validação
    btn = ft.ElevatedButton(
        text="Login",
        width=125,
        on_click=lambda _: validar_login(usuario, senha, page)
    )

    # Container do formulário de login
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

# Páginas correspondentes ao nível de segurança 1
def nivel1_page(page):
    page.title = "Áreas Restritas Nível 1 - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.WHITE

    container_1 = ft.Container(
        content=ft.ElevatedButton(text="Área Comum", width=400, height=100, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")  # Redireciona para a página de acesso permitido
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

    container_3 = ft.Container(
        content=ft.ElevatedButton(text="Sala de Controle", width=400, height=100, style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN, color=ft.colors.WHITE, text_style=ft.TextStyle(size=30)),
            on_click=lambda _: page.go("/acesso-permitido")
        ),
        alignment=ft.alignment.center,
        border_radius=10
    )

    container_4 = ft.Container(
        content=ft.ElevatedButton(text="Cofre", width=400, height=100, style=ft.ButtonStyle(
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
            controls=[container_1, container_2, container_3, container_4],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()
    page.add(container_pai)

# Páginas correspondentes ao nível de segurança 2
def nivel2_page(page):
    page.title = "Áreas Restritas Nível 2 - Wayne Industries"
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

    container_3 = ft.Container(
        content=ft.ElevatedButton(text="Sala de Controle", width=400, height=100, style=ft.ButtonStyle(
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
            controls=[container_1, container_2, container_3],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()
    page.add(container_pai)

# Páginas correspondentes ao nível de segurança 3
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
        alignment=ft.alignment.center,
        padding=10
    )

    page.controls.clear()
    page.add(container_pai)

# Página de "Acesso Permitido"
def acesso_permitido_page(page):
    page.title = "Acesso Permitido - Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK

    acesso_text = ft.Text(
        "ACESSO PERMITIDO", 
        size=50, 
        color=ft.colors.GREEN,
        weight=ft.FontWeight.BOLD
    )

    container = ft.Container(
        content=acesso_text,
        alignment=ft.alignment.center,
        padding=20
    )

    page.controls.clear()
    page.add(container)

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
            
    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)