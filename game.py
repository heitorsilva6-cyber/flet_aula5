import flet as ft

def main(page: ft.Page):
    mensagem = ft.Text("Escolha a opção correta!")
    resposta_correta = "Gato"
    page.bgcolor = "#9000FF"

    def verificar_resposta(e):
        if e.control.content == resposta_correta:
            mensagem.value = "Parabéns"
        else:
            mensagem.value = "Resposta errada"
        page.update()

    page.title = "Game: Adivinhe a imagem"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "Adivinhe a Imagem",
                    size=24,
                    weight="bold",
                    color="#FF007B"
                ),
                ft.Image(
                    src="imagens/gatinho.jpg",
                    height=200
                ),
                ft.Row(
                    controls=[
                        ft.Button(
                            content="Cachorro",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Gato",
                            on_click=verificar_resposta
                        ),
                        ft.Button(
                            content="Coelho",
                            on_click=verificar_resposta
                        ),
                    ],
                     alignment = ft.MainAxisAlignment.CENTER

                ),
                mensagem
            ],
            horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
    )

ft.run(main)