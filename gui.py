from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import time

# import tk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\54793421857\Desktop\Tela\Tela_Projeto_TKinter-main\tela\Imagem")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = tk.Tk()
window.geometry("978x636")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=636, width=978, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Imagens

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    713.0,
    481.0,
    image=image_image_8
)

ImagemBotaoVoltarA = PhotoImage(
    file=relative_to_assets("VoltarAzul.png"))

ImagemTitulo = PhotoImage(
    file=relative_to_assets("Titulo.png"))

ImagemTextoAzul = PhotoImage(
    file=relative_to_assets("TextoAzul.png"))

ImagemQDU = PhotoImage(
    file=relative_to_assets("QDU.png"))

ImagemBotaoFinalizar = PhotoImage(
    file=relative_to_assets("Finalizar.png"))

ImagemTextoAnexar = PhotoImage(
    file=relative_to_assets("TextoAnexar.png"))

ImagemQDUSF = PhotoImage(
    file=relative_to_assets("QDUSF.png"))

ImagemBGCT1 = PhotoImage(
    file=relative_to_assets("BGCT.png"))

ImagemCaixaTexto1 = PhotoImage(
    file=relative_to_assets("CaixaTexto.png"))

ImagemBGCT2 = PhotoImage(
    file=relative_to_assets("BGCT.png"))

ImagemCaixaTexto2 = PhotoImage(
    file=relative_to_assets("CaixaTexto.png"))

# Botoes

BotaoVoltarAzul = Button(
    image=ImagemBotaoVoltarA,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("voltar clicked"),
    relief="flat"
)

BotaoVoltarAzul.place(
    x=126.0,
    y=550.0,
    width=173.0,
    height=58.0
)

BotaoFinalizar = Button(
    image=ImagemBotaoFinalizar,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Finalizar clicked"),
    relief="flat"
)

BotaoFinalizar.place(
    x=627.0,
    y=551.0,
    width=172.0,
    height=56.0
)

# texto

Titulo = canvas.create_image(
    723.0,
    67.0,
    image=ImagemTitulo
)

TextoAzul = canvas.create_image(
    224.0,
    318.0,
    image=ImagemTextoAzul
)

QDU = canvas.create_image(
    613.0,
    178.0,
    image=ImagemQDU
)

TextoAnexar = canvas.create_image(
    639.0,
    424.0,
    image=ImagemTextoAnexar
)

QUDSF = canvas.create_image(
    723.0,
    301.0,
    image=ImagemQDUSF
)

BGCT1 = canvas.create_image(
    713.0,
    239.0,
    image=ImagemBGCT1
)

BGCT2 = canvas.create_image(
    713.0,
    362.0,
    image=ImagemBGCT2
)

# Caixas de texto

CaixaTexto1 = canvas.create_image(
    713.0,
    240.0,
    image=ImagemCaixaTexto1
)
CaixaTexto1 = Text(
    bd=0,
    bg="#E2E2E2",
    fg="#000716",
    highlightthickness=0
)
CaixaTexto1.place(
    x=625.0,
    y=213.0,
    width=176.0,
    height=52.0
)

CaixaTexto2 = canvas.create_image(
    713.0,
    363.0,
    image=ImagemCaixaTexto2
)

CaixaTexto2 = Text(
    bd=0,
    bg="#E2E2E2",
    fg="#000716",
    highlightthickness=0
)
CaixaTexto2.place(
    x=625.0,
    y=336.0,
    width=176.0,
    height=52.0
)

# Drop Drow

planilhas = {}


def abrir_arquivo_excel(opcao):
    file_paths = filedialog.askopenfilenames(filetypes=[("Arquivos Excel", "*.xlsx")])
    if file_paths:
        planilhas[opcao] = []
        for file_path in file_paths:
            # Abra e leia a planilha
            workbook = openpyxl.load_workbook(file_path)
            planilhas[opcao].append(workbook)
            # Feche a planilha (se necessário)
            workbook.close()


opcoes = ["Reclassificação ", "Doc. Pessoais", "Nome da mãe", "Relatorio Hora Extra", "Relatorio de férias",
          "Deligamento de benefício", "Planinha de exceções"]

var_opcao = tk.StringVar(window)
var_opcao.set(opcoes[0])


def opcao_selecionada(*args):
    opcao = var_opcao.get()
    print(f"Opção selecionada: {opcao}")
    abrir_arquivo_excel(opcao)
    print(planilhas)
    messagebox.showinfo('Sucesso', f'Sucesso em adicionar planilha: {opcao}')



image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))


menu_suspenso = tk.OptionMenu(window, var_opcao, *opcoes, command=opcao_selecionada)
menu_suspenso.pack()
menu_suspenso.configure(anchor="n")
canvas.create_window(713.0, 481.0, window=menu_suspenso)


window.resizable(False, False)
window.mainloop()