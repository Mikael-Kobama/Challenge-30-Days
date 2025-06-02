from tkinter import *
from tkinter import Tk, ttk

# importando pillow
from PIL import Image, ImageTk

c0  = "#FF0000"  # Vermelho
c1  = "#00FF00"  # Verde
c2  = "#0000FF"  # Azul
c3  = "#FFFF00"  # Amarelo
c4  = "#FF00FF"  # Magenta
c5  = "#00FFFF"  # Ciano
c6  = "#FFFFFF"  # Branco
c7  = "#000000"  # Preto
c8  = "#808080"  # Cinza médio
c9  = "#FFA500"  # Laranja
c10 = "#800080"  # Roxo
c11 = "#008080"  # Verde-azulado (teal)


#criando janela
janela = Tk()
janela.title("")
janela.geometry("250x400")
janela.configure(background=c6)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Frames

frameCima = Frame(janela, width=300, height=50, bg=c6, relief="flat")
frameCima.grid(row=0, column=0)
frameMeio = Frame(janela, width=300, height=90, bg=c8, relief="flat")
frameMeio.grid(row=1, column=0)
frameBaixo = Frame(janela, width=300, height=290, bg=c6, relief="flat")
frameBaixo.grid(row=2, column=0)

# Logo

app_ = Label(frameCima, text="Orçamento", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=("Verdana 20"), bg=c6, fg=c4)
app_.place(x=0, y=0)


janela.mainloop()
