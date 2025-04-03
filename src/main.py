import flet as ft
from flet import AppBar, ElevatedButton, Text, Colors, View, Icons
from flet.core.text_style import TextStyle
from flet.core.textfield import TextField


def main(page: ft.Page):
    # Configuração da página
    page.title = 'Atividade 1 Navegação'
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Definição de funções

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                '/',
                [
                AppBar(title=Text('Home'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Icon(name=Icons.ATTACH_MONEY_ROUNDED, color="#191970", size=100),
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
                                               bgcolor="#191970",
                                               on_click=lambda _: page.go('/simular_aposentadoria')),
                                ElevatedButton(text='Ver regras',
                                               width=(page.window.width / 2),
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

                ], #controls
                bgcolor="#C6E2FF",
            )
        )
        if page.route == '/regras':
            page.views.append(
                View(
                    '/regras',
                    [
                        AppBar(title=Text('Regras'), color="#C6E2FF", bgcolor="#191970", center_title=True),
                        ft.Container(
                            content=ft.Column(
                                [
                                    Text(value='• Aposentadoria por idade', size=24, weight=ft.FontWeight.BOLD),
                                    Text(value='- Homens', size=22, weight=ft.FontWeight.BOLD, italic=True),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,  # Alinha no centro verticalmente
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Alinha no centro horizontalmente
                            ), #Column
                            alignment=ft.alignment.center,  # Centraliza o Container
                            padding=ft.padding.only(top=50)  # Ajuste para mover um pouco para baixo
                        ) #Container
                    ] #controls
                ) # View
            )
        page.update()

    def volta(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.go(page.route)
    page.on_view_pop = volta

    #     Criação de componentes

ft.app(main)