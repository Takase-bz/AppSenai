import asyncio
import flet
from flet import ThemeMode, View, Colors, TextField, Text, Button, Container, Column, Row, Icon, Icons, \
    ListView, ListTile, PopupMenuButton, PopupMenuItem, FloatingActionButton, Dropdown, DropdownOption


class Player:
    def __init__(self, modelo, apelido, bateria, armazenamento_usado, armazenamento_max, tipo):
        self.modelo = modelo
        self.apelido = apelido
        self.bateria = bateria
        self.armazenamento_usado = armazenamento_usado
        self.armazenamento_max = armazenamento_max
        self.tipo = tipo


def main(page: flet.Page):
    page.title = "Player Música"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista = []
    item_selecionado = None

    def navegar(route):
        asyncio.create_task(page.push_route(route))

    def excluir(item):
        lista.remove(item)
        montar_lista_padrao()

    def ver_detalhes(item):
        nonlocal item_selecionado
        item_selecionado = item
        navegar("/detalhes")

    def icone_tipo(tipo):
        return Icon(Icons.DEVICES if tipo == "Físico" else Icons.CLOUD, color=Colors.GREEN_300)

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista:
            list_view.controls.append(
                ListTile(
                    leading=icone_tipo(item.tipo),
                    title=Text(item.modelo),
                    subtitle=Text(item.apelido),
                    trailing=PopupMenuButton(
                        items=[
                            PopupMenuItem(
                                "Detalhes",
                                icon=Icon(Icons.REMOVE_RED_EYE),
                                on_click=lambda e, item=item: ver_detalhes(item)
                            ),
                            PopupMenuItem(
                                "Excluir",
                                icon=Icon(Icons.DELETE),
                                on_click=lambda e, item=item: excluir(item)
                            ),
                        ]
                    )
                )
            )

    def salvar(e):
        if (
            input_modelo.value and input_apelido.value and input_bateria.value and
            input_armasenamento_usado.value and input_armasenamento_max.value and input_tipo.value
        ):
            lista.append(
                Player(
                    input_modelo.value,
                    input_apelido.value,
                    input_bateria.value,
                    input_armasenamento_usado.value,
                    input_armasenamento_max.value,
                    input_tipo.value
                )
            )

            input_modelo.value = ""
            input_apelido.value = ""
            input_bateria.value = ""
            input_armasenamento_usado.value = ""
            input_armasenamento_max.value = ""
            input_tipo.value = None

            montar_lista_padrao()
            navegar("/lista")

    def route_change(e=None):
        page.views.clear()

        # LISTA
        if page.route == "/lista":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista",
                    controls=[
                        flet.AppBar(title="Lista Players", bgcolor=Colors.PURPLE_600),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda _: navegar("/cadastro")
                    )
                )
            )

        # CADASTRO
        elif page.route == "/cadastro":
            page.views.append(
                View(
                    route="/cadastro",
                    controls=[
                        flet.AppBar(title="Cadastro Player", bgcolor=Colors.PURPLE_600),

                        input_modelo,
                        input_apelido,
                        input_bateria,
                        input_armasenamento_usado,
                        input_armasenamento_max,
                        input_tipo,

                        Button("Salvar", on_click=salvar)
                    ]
                )
            )

        # DETALHES (COM BOTÃO VOLTAR)
        elif page.route == "/detalhes":
            page.views.append(
                View(
                    route="/detalhes",
                    controls=[
                        flet.AppBar(
                            title="Detalhes",
                            bgcolor=Colors.PURPLE_600,
                            leading=flet.IconButton(
                                icon=Icons.ARROW_BACK,
                                on_click=lambda _: page.go("/lista")
                            )
                        ),

                        Container(
                            content=Column([
                                Row([Icon(Icons.DEVICES), Text(item_selecionado.modelo)]),
                                Row([Icon(Icons.PERSON), Text(item_selecionado.apelido)]),
                                Row([Icon(Icons.BATTERY_FULL), Text(item_selecionado.bateria)]),
                                Row([Icon(Icons.SD_STORAGE), Text(item_selecionado.armazenamento_usado)]),
                                Row([Icon(Icons.SD_STORAGE_OUTLINED), Text(item_selecionado.armazenamento_max)]),
                                Row([Icon(Icons.CATEGORY), Text(item_selecionado.tipo)]),
                            ]),
                            bgcolor=Colors.PURPLE_500,
                            padding=15,
                            border_radius=10
                        )
                    ]
                )
            )

        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # CAMPOS
    input_modelo = TextField(label="Modelo")
    input_apelido = TextField(label="Apelido")
    input_bateria = TextField(label="Bateria")
    input_armasenamento_usado = TextField(label="Armazenamento usado")
    input_armasenamento_max = TextField(label="Armazenamento máximo")

    input_tipo = Dropdown(
        label="Tipo",
        options=[
            DropdownOption("Físico"),
            DropdownOption("Virtual")
        ]
    )

    list_view = ListView()

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/lista")


flet.run(main)