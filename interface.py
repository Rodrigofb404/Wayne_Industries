import flet as ft

def main(page: ft.Page):
    page.title = "Wayne Industries"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.GREY_50
    
    img = ft.Image(
        src="wayne_logo.png",
        width="250",
        height="100",
        fit=ft.ImageFit.CONTAIN
    )
    titulo = ft.Text("Wayne Industries", size=50, color="Black") 

    usuario = ft.TextField(
        label="Usuário", 
        autofocus=True, 
        width=250,
        border_color=ft.colors.WHITE)
    senha = ft.TextField(
        label="Senha",
        password=True, 
        width=250,
        border_color=ft.colors.WHITE)
    btn = ft.ElevatedButton(text="Login", width=125)

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

ft.app(target=main)
