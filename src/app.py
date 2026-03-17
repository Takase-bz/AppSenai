import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment
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
            text.value = f' Numero {numero} Par'
            page.update()
        else:
            text.value = f' Numero {numero} Impar'
            page.update()

    def verificar_idade():
        #data atual
        date_now = datetime.today()
        #data inserida
        data_nasc = int(input_data_nasc.value)

        resultado_idade = date_now - data_nasc
        if resultado_idade <= 18:
            f''



    # Componentes
    text = Text()
    edit_text = TextField(label="Nome")
    sobrenome_text = TextField(label="Sobrenome", on_blur=salvar_nome)
    input_numero = TextField(label="numero", on_blur=verificacao_numero)
    input_data_nasc = TextField(hint_text="Data de nascimento", on_blur=verificar_idade)
    btn_salvar = OutlinedButton("Salvar", on_click=salvar_nome)




    # Construção da tela
    page.add(
        Column(
         [
             edit_text,
             sobrenome_text,
             btn_salvar,
             input_numero,


             text
         ],
         width=400,
         horizontal_alignment=CrossAxisAlignment.CENTER
         )
    )




flet.app(main)
