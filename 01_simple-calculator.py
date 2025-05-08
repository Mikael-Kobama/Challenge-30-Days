import flet as ft

def main(page: ft.Page):
  page.title = "Calculator"
  page.bgcolor = "#2d2d2d"
  page.window.width = 350
  page.window.height = 470


  all_values = ""

  result_text = ft.Text(value = "0", size = 28, color = "white", text_align = "right")

  def input_value(e):
    nonlocal all_values
    all_values+= str(e.control.text)
    result_text.value = all_values
    page.update()

  def clean_screen(e):
    nonlocal all_values
    all_values= ""
    result_text.value = "0"
    page.update()

  def calculate(e):
    nonlocal all_values
    try:
      result_text.value = str(eval(all_values))
      all_values = result_text.value
    except:
      result_text.value = "Error"
      all_values = ""
    page.update()

  display =  ft.Container(
    content = result_text,
    bgcolor = "#37474f",
    padding=10,
    border_radius=10,
    height=10,
    alignment=ft.alignment.center_right

  )

  # estilizacao dos botoes

  style_numbers = {
    "height": 60,
    "bgcolor": "#4d4d4d",
    "color": "white",
    "expand": 1,
  }

  style_operators = {
    "height": 60,
    "bgcolor": "#FF9500",
    "color": "white",
    "expand": 1,
  }
  style_clean = {
    "height": 60,
    "bgcolor": "#FF3B30",
    "color": "white",
    "expand": 1,
  }
  style_equal = {
    "height": 60,
    "bgcolor": "#34c759",
    "color": "white",
    "expand": 1,
  }

  table_of_buttons = [
    [
      ("C", style_clean, clean_screen),
      ("%", style_operators, input_value),
      ("/", style_operators, input_value),
      ("*", style_operators, input_value)
    ],
    [
      ("7", style_numbers, input_value),
      ("8", style_numbers, input_value),
      ("9", style_numbers, input_value),
      ("-", style_operators, input_value)
    ],
    [
      ("4", style_numbers, input_value),
      ("5", style_numbers, input_value),
      ("6", style_numbers, input_value),
      ("+", style_operators, input_value)
    ],
    [
      ("1", style_numbers, input_value),
      ("2", style_numbers, input_value),
      ("3", style_numbers, input_value),
      ("=", style_equal, calculate)
    ],
    [
      ("0", {**style_numbers, "expand":2}, input_value),
      (".", style_numbers, input_value),
      ("X", style_operators, lambda e: None )
    ],

  ]

  buttons = []

  for line in table_of_buttons:
    line_control = []
    for text, style, handler in line:
      btn = ft.ElevatedButton(
        text=text,
        on_click=handler,
        **style,
        style=ft.ButtonStyle(
          shape=ft.RoundedRectangleBorder(radius=5),
          padding=5
        )
        
      )
      line_control.append(btn)
    buttons.append(ft.Row(line_control, spacing=5))
    


  page.add(
    ft.Column(
      [
        display,
        ft.Column(buttons, spacing=5)
      ]
    )
  )

ft.app(target=main)

