import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, ElevatedButton, Text, FloatingActionButton, Icons, \
    ListView, Card, Column, Row, Icon, ListTile, PopupMenuPosition, PopupMenuButton, PopupMenuItem


# EXERCICIO 1 MENSAGEM COM O NOME



def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de listas"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # FUNÇÕES
    #  def msg_nome():
    #     text_msg = Text(f"Bom dia {input_nome.value}")
    #      input_nome.value = ""
    #      navegar("/tela_msg")

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()



        for item in lista_dados:
            list_view.controls.append(
                Text(item)
            )

    def montar_lista_padrao():
        list_view.controls.clear()



        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(icon=Icons.PERSON, color=Colors.PURPLE_400),
                    title=item,
                    subtitle="subtitulo",
                    trailing=PopupMenuButton(
                        icon=Icon(icon=Icons.ADD, color=Colors.PURPLE_400),
                        items=[
                            PopupMenuItem("Ver Detalhes", icon=Icon(icon=Icons.REMOVE_RED_EYE, color=Colors.PURPLE_400)),
                            PopupMenuItem("Editar", icon=Icon(icon=Icons.EDIT_OUTLINED, color=Colors.PURPLE_400)),
                            PopupMenuItem("Excluir", icon=Icon(icon=Icons.DELETE, color=Colors.PURPLE_400,), on_click=lambda: excluir(item)),
                        ]
                    )
                )
            )

    def montar_lista_card():
        list_view.controls.clear()



        for item in lista_dados:
            list_view.controls.append(
                Card(
                    width=120,
                    height=50,
                    content=Row(
                        [
                                Icon(Icons.PERSON, color=Colors.PURPLE_400),
                                Text(item)
                        ],
                        margin=8
                    )

                )
            )
    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()



    def salvar_dados():
        nome = input_nome.value.strip()


        nome = input_nome.value

        if nome:
            lista_dados.append(nome)
            input_nome.error = None
        else:
            input_nome.error = "Campo Obrigatorio"


        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()

    # COMPONENTES


    # btn_salvar = ElevatedButton("Salvar", on_click=nome)

    # gerenciar telas(routes)
    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="exemplo de listas",
                        bgcolor=Colors.PURPLE_600
                    ),
                    # Text("Digite seu nome"),
                    # btn_salvar,
                    Button("lista de texto", on_click=lambda: navegar("/lista_text"), color=Colors.PURPLE_400),
                    Button("lista de card", on_click=lambda: navegar("/lista_card"), color=Colors.PURPLE_400),
                    Button("lista padrão android", on_click=lambda: navegar("/lista_padrao"), color=Colors.PURPLE_400)

                ]
            )
        )

        if page.route == "/lista_text":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_text",
                    controls=[
                        flet.AppBar(
                            title="Lista de texts",
                            bgcolor=Colors.PURPLE_600
                    ),
                        input_nome,
                        btn_salvar,
                        list_view

                    ],
                    floating_action_button=FloatingActionButton(
                        Icon(Icons.ADD, color=Colors.PURPLE_400),
                    )
                )
            )
        elif page.route == "/lista_card":
            montar_lista_card()
            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        flet.AppBar(
                            title="Lista de cards",
                            bgcolor=Colors.PURPLE_600
                        ),
                        input_nome,
                        btn_salvar,
                        list_view

                    ]
                )
            )
        elif page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(
                            title="lista padrão android",
                            bgcolor=Colors.PURPLE_600
                        ),
                        list_view

                    ],
                    floating_action_button=FloatingActionButton(
                        Icon(Icons.ADD, color=Colors.PURPLE_400),
                        on_click=lambda: navegar("/form_cadastro")
                    ),

                )
            )

        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Cadastro",
                            bgcolor=Colors.PURPLE_600
                        ),
                        input_nome,
                        btn_salvar,


                    ]
                )
            )
    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    #Componentes
    input_nome = TextField(label="Digite seu nome", on_submit=salvar_dados)

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    list_view = ListView(height=500)

    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
