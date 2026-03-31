import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, ElevatedButton, Text, Container, Column, Row, Icon, Icons, \
    Alignment, CrossAxisAlignment

#EXERCICIO 3 POO PLAYER MUSCIA
def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # FUNÇÕES
    def player_musica():
        text_modelo.value = input_modelo.value
        text_apelido.value = input_apelido.value
        text_bateria.value = input_bateria.value
        text_armasenamento_usado.value = input_armasenamento_max.value
        text_armasenamento_max.value = input_armasenamento_usado.value

        tem_erro = False

        if input_modelo.value:
            input_modelo.error = None
        else:
            tem_erro = True
            input_modelo.error = " Modelo obrigatorio"
        if input_apelido.value:
            input_apelido.error = None
        else:
            tem_erro = True
            input_apelido.error = "apelido obrigatorio"

        if input_bateria.value:
            input_bateria.error = None
        else:
            tem_erro = True
            input_bateria.error = "Bateria obrigatorio"
        if text_armasenamento_max.value:
            text_armasenamento_max.error = None
        else:
            tem_erro = True
            text_armasenamento_max.error = "Armasenamento maximo obrigatorio"

        if text_armasenamento_usado.value:
            text_armasenamento_usado.error = None
        else:
            tem_erro = True
            text_armasenamento_usado.error = "Armasenamento utilizado obrigatorio"

        if not tem_erro:
            input_modelo.value = ""
            input_apelido.value = ""
            input_bateria.value = ""
            input_armasenamento_max.value = ""
            input_armasenamento_usado.value = ""
            navegar("/Player_musica")

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # gerenciar telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Cadastro Funcionario",
                        bgcolor=Colors.PURPLE_600
                    ),
                    Text("Preencha os Campos"),
                    input_modelo,
                    input_apelido,
                    input_bateria,
                    input_armasenamento_usado,
                    input_armasenamento_max,
                    btn_salvar,

                ]
            )
        )

        if page.route == "/Player_musica":
            page.views.append(
                View(
                    route="/Player_musica",
                    controls=[
                        flet.AppBar(
                            title="Player de Musica",
                            bgcolor=Colors.PURPLE_600
                        ),
                        Container(
                            Column([
                                text_modelo,
                                Row([
                                    Icon(Icons.LIBRARY_MUSIC, color=Colors.PURPLE_200, size=30),
                                    text_apelido,

                                ]),
                                Row([
                                    Icon(Icons.BATTERY_CHARGING_FULL_ROUNDED, color=Colors.PURPLE_200, size=30),
                                    text_bateria,
                                ]),
                                Row([
                                    Icon(Icons.SD_STORAGE_OUTLINED, color=Colors.PURPLE_200, size=30),
                                    text_armasenamento_max,
                                ]),
                                Row([
                                    Icon(Icons.SD_STORAGE_SHARP, color=Colors.PURPLE_200, size=30),
                                    text_armasenamento_usado,
                                ]),
                            ],
                            horizontal_alignment = CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=Colors.PURPLE_500,
                            padding=15,
                            border_radius=10,
                            width=400,
                        )
                    ]

                )

            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # COMPONENTES
    input_modelo = TextField(label="Digite o modelo ")
    input_apelido = TextField(label="Digite o apelido ")
    input_bateria = TextField(label="Digite a bateria ")
    input_armasenamento_usado = TextField(label="Digite o armasenamento utilizado ")
    input_armasenamento_max = TextField(label="Digite o armasenamento maximo ")

    text_modelo = Text()
    text_apelido = Text()
    text_bateria = Text()
    text_armasenamento_max = Text()
    text_armasenamento_usado = Text()

    btn_salvar = ElevatedButton("Salvar", on_click=player_musica)

    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
