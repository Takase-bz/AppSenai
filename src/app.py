from operator import contains

import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight
from datetime import datetime



def main(page: flet.Page):
    # Configurações
    page.title = "Primeiro APP"
    page.theme_mode = ThemeMode.DARK  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700
    # Funções
    def salvar_nome():
        text.value = f"Bom Dia {edit_text.value} {sobrenome_text.value}"
        page.update()

    def verificacao_numero():
        numero = int(input_numero.value)
        if numero % 2 == 0:
            text_parimpar.value = f' Numero {numero} Par'
            page.update()
        else:
            text_parimpar.value = f' Numero {numero} Impar'
            page.update()

    def nascimento():
        ano_nascimento = int(input_nascimento.value)
        idade = datetime.today().year - ano_nascimento

        if idade >= 18:
            text_nascimento.value = f"ele é maior de idade, {idade} anos"
            page.update()
        else:
            text_nascimento.value = f"ele é menor de idade, {idade} anos"
            page.update()



    # Componentes
    text = Text()
    text_parimpar = Text()
    text_nascimento = Text()
    edit_text = TextField(label="Nome")
    sobrenome_text = TextField(label="Sobrenome", on_blur=salvar_nome)
    input_numero = TextField(label="numero", on_blur=verificacao_numero, hint_text="verifique se é par ou impar")
    input_nascimento = TextField(hint_text="data de nascimento", on_blur=nascimento)
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)
    btn_numero = OutlinedButton("Verificar", on_click=verificacao_numero)




    # Construção da tela
    page.add(
        Column(
         [
            Container(
                Column(
                    [
                        Text( "atividade 1", weight=FontWeight.BOLD,size=24),
                        edit_text,
                        sobrenome_text,
                        btn_salvar,
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),

                bgcolor=Colors.PURPLE_500,
                padding=15,
                border_radius=10,
                width=400,

            ),

             Container(
                 Column(
                     [
                         Text("atividade 2", weight=FontWeight.BOLD, size=24),
                         input_numero,
                     ],
                     horizontal_alignment=CrossAxisAlignment.CENTER,
                 ),

                 bgcolor=Colors.PURPLE_500,
                 padding=15,
                 border_radius=10,
                 width=400,

             ),
             Container(
                 Column(
                     [
                         Text("atividade 3", weight=FontWeight.BOLD, size=24),
                         input_nascimento,
                     ],
                     horizontal_alignment=CrossAxisAlignment.CENTER,
                 ),

                 bgcolor=Colors.PURPLE_500,
                 padding=15,
                 border_radius=10,
                 width=400,

             ),


             text,
             text_parimpar,
             text_nascimento
         ],
         width=400,
         horizontal_alignment=CrossAxisAlignment.CENTER
         )
    )




flet.run(main)
