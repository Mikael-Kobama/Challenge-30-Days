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

# Criando janela
janela = Tk()
janela.title("Calculadora 50-30-20")
janela.geometry("250x400")
janela.configure(background=c6)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Frames
frameCima = Frame(janela, width=300, height=50, bg=c6)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=300, height=90, bg=c1)
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela, width=300, height=290, bg=c6)
frameBaixo.grid(row=2, column=0)

# Logo
app_img = Image.open("login.jpg")
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento", compound=LEFT,
                 padx=5, font=("Verdana", 18, "bold"), bg=c6, fg=c4)
app_logo.place(x=0, y=5)

app_linha = Label(frameCima, width=295, height=1, bg=c3)
app_linha.place(x=0, y=47)


# Função Calcular

def calcular():
  renda_mendal = float(e_valor.get())

  obtendo_50_porcento = (50 / 100) * renda_mendal
  obtendo_30_porcento = (30 / 100) * renda_mendal
  obtendo_20_porcento = (20 / 100) * renda_mendal

  print("=================\nSeus Numeros de 50% 30% 20%\n=================")

  l_necessidade["text"] = ("R${:,.2f}".format(obtendo_50_porcento))
  l_gastos["text"] =("R${:,.2f}".format(obtendo_30_porcento))
  l_gastos_poupa["text"] =("R${:,.2f}".format(obtendo_20_porcento))

  print("==================================")

# Frame Meio
Label(frameMeio, text="Digite sua renda mensal:", bg=c1, fg=c4, font=("Ivy", 10)).place(x=7, y=10)

e_valor = Entry(frameMeio, width=15, font=("Ivy", 14), justify="center", relief="solid", bg=c2)
e_valor.place(x=10, y=35)

b_calcular = Button(frameMeio, command=calcular, text="CALCULAR", overrelief=RIDGE, font=("Ivy", 10, "bold"),
                    bg=c0, fg=c2)
b_calcular.place(x=140, y=35)

# Frame Baixo
Label(frameBaixo, text="Distribuição 50% / 30% / 20%", bg=c6, fg=c5, font=("Verdana", 10, "bold")).place(x=10, y=10)

# Necessidades
Label(frameBaixo, text="Necessidades (50%)", bg=c6, fg=c4, font=("Verdana", 10)).place(x=10, y=50)
l_necessidade = Label(frameBaixo, text="R$ 0,00", bg=c8, fg=c0, font=("Verdana", 12), width=22, anchor="w")
l_necessidade.place(x=10, y=75)

# Gastos supérfluos
Label(frameBaixo, text="Gastos supérfluos (30%)", bg=c6, fg=c4, font=("Verdana", 10)).place(x=10, y=115)
l_gastos = Label(frameBaixo, text="R$ 0,00", bg=c8, fg=c0, font=("Verdana", 12), width=22, anchor="w")
l_gastos.place(x=10, y=140)

# Poupanças
Label(frameBaixo, text="Poupança/Investimento (20%)", bg=c6, fg=c4, font=("Verdana", 10)).place(x=10, y=180)
l_gastos_poupa = Label(frameBaixo, text="R$ 0,00", bg=c8, fg=c0, font=("Verdana", 12), width=22, anchor="w")
l_gastos_poupa.place(x=10, y=205)

janela.mainloop()
