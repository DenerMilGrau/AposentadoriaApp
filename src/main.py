import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Icons
from flet.core import slider
from flet.core.list_view import ListView
from flet.core.text_style import TextStyle
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Atividade 1 Navegação'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 375
    page.window.height = 667

    page.theme = ft.Theme(
        text_theme=ft.TextTheme(
            body_medium=TextStyle(color="#191970")
        ) # Define a cor padrão dos textos como azul escuro
    )

    # Definição de funções

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                    AppBar(title=Text('Simulador de aposentadoria'), color="#C6E2FF", bgcolor="#191970", center_title=True),

                    ft.Container(
                        content=ft.Column(
                            [
                                # ft.Icon(name=Icons.ATTACH_MONEY_ROUNDED, color="#191970", size=100),
                                ft.Image(src=f"inss.png",
                                         width=(page.window.width / 2),
                                         fit=ft.ImageFit.CONTAIN)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha no centro horizontalmente
                        ),
                        alignment=ft.alignment.center,  # Centraliza o Container
                        padding=ft.padding.only(top=80)  # Ajuste para mover um pouco para baixo
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ElevatedButton(text='Simular aposentadoria',
                                               width=(page.window.width / 2),
                                               color="#C6E2FF",
                                               bgcolor="#191970",
                                               on_click=lambda _: page.go('/simular_aposentadoria')),
                                ElevatedButton(text='Ver regras',
                                               width=(page.window.width / 2),
                                               color="#C6E2FF",
                                               bgcolor="#191970",
                                               on_click=lambda _: page.go('/regras')
                                               )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha no centro horizontalmente
                        ),
                        alignment=ft.alignment.center,  # Centraliza o Container
                        padding=ft.padding.only(top=80)  # Ajuste para mover um pouco para baixo
                    )

                ],  # controls
                bgcolor="#C6E2FF",
            )
        )
        if page.route == '/regras':
            page.views.append(
                View(
                    '/regras',
                    [
                        AppBar(title=Text('Regras'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                        ft.ListView(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            Text(value='• Aposentadoria por idade', size=24, weight=ft.FontWeight.BOLD),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Text(value='- Homens', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='65 anos de idade e pelo menos 15 anos de contribuição.',
                                                                        size=16),
                                                                ]
                                                            ),  # Column 3
                                                            padding=ft.padding.only(left=40)
                                                        ),  # Container 3

                                                        Text(value='- Mulheres', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='62 anos de idade e pelo menos 15 anos de contribuição.',
                                                                        size=16)
                                                                ]
                                                            ),  # COlumn 4
                                                            padding=ft.padding.only(left=40)
                                                        )  # Column 4
                                                    ]
                                                ),  # column 2 D
                                                padding=ft.padding.only(left=20)
                                            ),  # container 2 C

                                            Text(value='• Aposentadoria por tempo de contribuição', size=20,
                                                 weight=ft.FontWeight.BOLD),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        Text(value='- Homens', size=20, weight=ft.FontWeight.BOLD,
                                                             italic=True),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(value='35 anos de contribuição.', size=16)
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        ),

                                                        Text(value='- Mulheres', size=20, weight=ft.FontWeight.BOLD),
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(value='30 anos de contribuição', size=16)
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        )

                                                    ]
                                                ),  # Column 5 D
                                                padding=ft.padding.only(left=20)
                                            ),  # Container 3 C

                                            Text(value='• Valor estimado do benefício', size=20,
                                                 weight=ft.FontWeight.BOLD),
                                            ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Container(
                                                            content=ft.Column(
                                                                [
                                                                    Text(
                                                                        value='O valor da aposentadoria será uma média de 60% da média salarial informada,'
                                                                              ' acrescido de 2% por ano que exceder o tempo mínimo de contribuição.',
                                                                        size=16)
                                                                ]
                                                            ),
                                                            padding=ft.padding.only(left=40)
                                                        )
                                                    ]
                                                )
                                            )
                                        ]
                                    ),  # Column B
                                    alignment=ft.alignment.center,  # Centraliza o Container
                                    # padding=ft.padding.only(top=50)  # Ajuste para mover um pouco para baixo
                                )  # Container A
                            ],
                            expand=True
                        ),

                    ],  # controls
                    bgcolor="#C6E2FF"
                )  # View
            )

        if page.route == '/simular_aposentadoria':
            page.views.append(
                View(
                    '/simular_aposentadoria',
                    [
                        AppBar(title=Text('Simular'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                        ft.ListView(
                            [
                                Text(value='Selecione sua idade:', size=22, weight=ft.FontWeight.BOLD),

                                slider_idade,
                                txt_idade,

                                Text(value='Selecione seu gênero:', size=22, weight=ft.FontWeight.BOLD),
                                radio_genero,
                                Text(value='Selecione seu tempo de contribuição:', size=22, weight=ft.FontWeight.BOLD),

                                slider_tempo_contribuicao,
                                txt_tempo_contribuicao,

                                Text(value='Selecione a categoria da aposentadoria desejada:', size=22, weight=ft.FontWeight.BOLD),
                                radio_categoria,

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ElevatedButton(text='Calcular',
                                                           width=(page.window.width / 2),
                                                           color="#C6E2FF",
                                                           bgcolor="#191970",
                                                           on_click=exibir_info)
                                                           # lambda _: page.go('/resultado'))
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                        # Alinha no centro horizontalmente
                                    ),
                                    padding=ft.padding.only(top=40)
                                )

                            ],
                            expand=True,
                        )
                    ],
                    bgcolor="#C6E2FF"

                )
            )
        page.update()

    def volta(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def slider_change_idade(e):
        txt_idade.value = f'IDADE: {int(e.control.value)}'
        page.update()

    def slider_change_tempo(e):
        txt_tempo_contribuicao.value = f'TEMPO DE CONTRIBUIÇÃO: {int(e.control.value)}'
        page.update()

    def exibir_info(e):
        print('radio genero', radio_genero.value)
        print('radio categoria', radio_categoria.value)
        print('tempo contribuicao', slider_tempo_contribuicao.value)
        print('idade', slider_idade.value)

    page.on_route_change = gerencia_rotas
    page.go(page.route)
    page.on_view_pop = volta

    #     Criação de componentes
    txt_idade = Text(value='IDADE: 18', size=20, weight=ft.FontWeight.BOLD, bgcolor="cyan")
    slider_idade = ft.Slider(min=18, max=100, divisions=82, label="{value}",
                                  overlay_color="dark_blue", active_color="cyan",
                                  inactive_color="grey", on_change=slider_change_idade)

    txt_tempo_contribuicao = Text(value='TEMPO DE CONTRIBUIÇÃO: 0', size=20, weight=ft.FontWeight.BOLD, bgcolor="cyan")
    slider_tempo_contribuicao = ft.Slider(min=0, max=90, divisions=90, label="{value}",
                             overlay_color="dark_blue", active_color="cyan",
                             inactive_color="grey", on_change=slider_change_tempo)

    radio_genero = ft.RadioGroup(content=ft.Column([
                                    ft.Radio(value="homem", label="Homem", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    }),
                                    ft.Radio(value="mulher", label="Mulher", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    })]))

    radio_categoria = ft.RadioGroup(content=ft.Column([
                                    ft.Radio(value="porIdade", label="Por idade", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    }),
                                    ft.Radio(value="porTempo", label="Por tempo de contribuição", fill_color={
                                        ft.ControlState.HOVERED: "#191970",
                                        ft.ControlState.DEFAULT: "cyan",
                                    })]))

ft.app(main)
