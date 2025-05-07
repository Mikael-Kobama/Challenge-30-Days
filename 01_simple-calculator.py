import flet as ft

def main(page: ft.Page):
  page.title = "Calculator"
  page.bgcolor = "#2d2d2d"
  page.window.width = 350
  page.window.higth = 470

  result_text = ft.Text(value = "0", size = 28, color = "white", text_align = "right")

  display =  ft.Container(
    content = result_text,
    bgcolor = "#37474f",
    padding=10,
    border_radius=10,
    heigth=10,
    alignment=ft.alignment.center_right

  )


  page.add(
    ft.Column(
      [
        display,
      ]
    )
  )


  ft.app(target=main)

