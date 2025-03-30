import flet as ft


def button_press(expression, button):
    if button == "AC":
        expression = "0"
    elif button == "=":
        try:
            expression = str(eval(expression.replace("^", "**")))
        except Exception:
            expression = "Помилка :("
    elif button == "R":
        if expression[0] == "-":
            expression = expression[1:]
        else:
            expression = "-" + expression
    elif button == "B":
        expression = expression[:-1]
        if expression == "":
            expression = "0"
    elif expression in ("0", "Помилка :(") and button not in ("+", "-", "*", "/", "^"):
        expression = button
    else:
        if expression[-1] == button and button in ("+", "-", "*", "/", "^"):
            expression = expression[:-1]
        expression += button

    return expression


def calculator(page: ft.Page):
    page.title = "Калькулятор"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.resizable = False
    page.window.width = 400
    page.window.height = 650
    display = ft.Text(value="0", text_align=ft.TextAlign.RIGHT, max_lines=1, size=30)
    buttons = [
        ["AC", "R", "^", "/"],
        ["7", "8", "9", "*"],
        ["4", "5", "6", "-"],
        ["1", "2", "3", "+"],
        ["0", ".", "B", "="],
    ]

    def on_click(e, display, page):
        display.value = button_press(display.value, e.control.data)
        page.update()

    def create_button(text, display, page, *args, **kwargs):
        button = ft.ElevatedButton(
            text=text,
            data=text,
            on_click=lambda e: on_click(e, display, page),
            width=80,
            height=80,
            *args,
            **kwargs,
        )
        if text == "B":
            button.content = ft.Icon(
                name=ft.Icons.BACKSPACE, color=ft.Colors.BLACK, size=18
            )
            button.text = None
        elif text == "R":
            button.content = ft.Icon(
                name=ft.Icons.REPLAY, color=ft.Colors.WHITE, size=18
            )
            button.text = None

        if text in ("+", "-", "*", "/", "="):
            button.bgcolor = ft.Colors.ORANGE
            button.color = ft.Colors.WHITE
        elif text in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "B"):
            button.bgcolor = ft.Colors.WHITE
            button.color = ft.Colors.BLACK
        else:
            button.bgcolor = ft.Colors.GREY
            button.color = ft.Colors.WHITE
        return button

    def route_change(route):
        page.views.clear()
        change2 = ft.IconButton(
            icon=ft.Icons.CALCULATE,
            on_click=lambda _: page.go("/advenced"),
            bgcolor=ft.Colors.WHITE,
            icon_color=ft.Colors.BLACK,
        )
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
                        title=ft.Text("Калькулятор", size=22, weight="bold"),
                        actions=[change2],
                    ),
                    ft.Column(
                        [display, ft.Divider(height=10)]
                        + [
                            ft.Row(
                                [create_button(char, display, page) for char in row],
                                alignment=ft.MainAxisAlignment.CENTER,
                                wrap=False,
                            )
                            for row in buttons
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ],
            )
        )
        if page.route == "/advenced":
            page.views.append(
                ft.View(
                    "/advenced",
                    [
                        ft.AppBar(
                            title=ft.Text("Просунутий Калькулятор", size=22, weight="bold"),
                        ),
                        ft.Column(
                            [display, ft.Divider(height=10)]
                            + [
                                ft.Row(
                                    [create_button(char, display, page) for char in row],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    wrap=False,
                                )
                                for row in buttons
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=calculator)
