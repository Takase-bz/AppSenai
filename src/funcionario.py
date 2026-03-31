import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, TextField, ElevatedButton, Text, Container

#EXERCICIO 2 FUNCIONARIO
def main(page: flet.Page):
    # CONFIGURAÇÕES
    page.title = "Exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # FUNÇÕES
    def exibir_mensagem():
        text_nome.value = input_nome.value
        text_CPF.value = input_CPF.value
        text_email.value = input_email.value
        text_salario.value = f" $ ,{input_salario.value}"

        tem_erro = False

        if input_nome.value:
            input_nome.error = None
        else:
            tem_erro = True
            input_nome.error = "Nome obrigatorio"
        if input_CPF.value:
            input_CPF.error = None
        else:
            tem_erro = True
            input_CPF.error = "CPF obrigatorio"
        if input_email.value:
            input_email.error = None
        else:
            tem_erro = True
            input_email.error = "Email obrigatorio"
        if input_salario.value:
            input_salario.error = None
        else:
            tem_erro = True
            input_salario.error = "Salario obrigatorio"

        if not tem_erro:
            input_nome.value = ""
            input_CPF.value = ""
            input_email.value = ""
            input_salario.value = ""
            navegar("/Funcionarios")

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
                    input_nome,
                    input_CPF,
                    input_email,
                    input_salario,
                    btn_salvar,

                ]
            )
        )

        if page.route == "/Funcionarios":
            page.views.append(
                View(
                    route="/Funcionarios",
                    controls=[
                        flet.AppBar(
                            title="Funcionarios",
                            bgcolor=Colors.PURPLE_600
                        ),
                            # text_msg
                            text_nome,
                            text_CPF,
                            text_email,
                            text_salario,


                    ],

                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # COMPONENTES
    input_nome = TextField(label="Digite seu nome")
    input_CPF = TextField(label="Digite seu CPF")
    input_email = TextField(label="Digite seu email")
    input_salario = TextField(label="Digite seu salario")
    text_nome = Text()
    text_CPF = Text()
    text_email = Text()
    text_salario = Text()

    btn_salvar = ElevatedButton("Salvar", on_click=exibir_mensagem)

    # EVENTOS
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
