import asyncio

import flet
from flet import ThemeMode, View, AppBar, Colors, Button

# MODELO NAVEGAÇÂO BASE, TODOS USAM
def main(page: flet.Page):
    #Configurar
    page.title = "exemplo de navegação"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)

        )




    # Gerenciar as telas(Routes)
    def route_chenge():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira Página",
                        bgcolor=Colors.PURPLE_500,



                    ),
                    Button("Ir para segunda tela", on_click= lambda : navegar("/segunda_tela")),

                ]
            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda Página",
                            bgcolor=Colors.PURPLE_500,

                        ),
                    ]
                )
            )


    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes



    # Eventos
    page.on_route_change = route_chenge
    page.on_view_pop = view_pop

    route_chenge()

flet.run(main)