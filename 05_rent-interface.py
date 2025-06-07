from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Cores harmoniosas
c0  = "#2E8B57"  # Verde escuro
c1  = "#F0F0F0"  # Cinza claro
c2  = "#FFFFFF"  # Branco
c3  = "#4682B4"  # Azul suave
c4  = "#333333"  # Cinza escuro
c5  = "#6A5ACD"  # Roxo claro
c6  = "#FAFAFA"  # Fundo neutro
c7  = "#000000"  # Preto
c8  = "#DCDCDC"  # Cinza médio


janela = Tk()
janela.title("")
janela.geometry("400x350")
janela.configure(background=c1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("cima")


# FRAMES -------
frameCima = Frame(janela, width=450, height=50, bg=c1, relief="flat")
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=100, bg=c1, relief="solid",)
framePergunta.grid(row=1, column=0, padx=5, sticky=NSEW)

frameResultado = Frame(janela, width=300, height=310, bg="#4E6E81", relief="raised")
frameResultado.grid(row=3, column=0, sticky=NSEW)

frameDia = Frame(frameResultado, width=200, height=100, bg=c1, relief="solid")
frameDia.grid(row=0, column=0, padx=1, pady=1, sticky=NSEW)

frameSemana = Frame(frameResultado, width=200, height=100, bg=c1, relief="solid")
frameSemana.grid(row=0, column=1, padx=1, pady=1, sticky=NSEW)

frameMes = Frame(frameResultado, width=200, height=100, bg=c1, relief="solid")
frameMes.grid(row=1, column=0, padx=1, pady=1, sticky=NSEW)

frameTotal = Frame(frameResultado, width=200, height=100, bg=c1, relief="solid")
frameTotal.grid(row=1, column=1, padx=1, pady=1, sticky=NSEW)


janela.mainloop()