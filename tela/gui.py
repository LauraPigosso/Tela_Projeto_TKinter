import tkinter
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\54793421857\Desktop\Tela\Tela_Projeto_TKinter\tela\Imagem")


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

CaixaTexto2.configure(font=("Arial", 14))
CaixaTexto1.configure(font=("Arial", 14))

def ValoresCaixa():
    valor_caixa1 = CaixaTexto1.get("1.0", "end-1c")
    valor_caixa2 = CaixaTexto2.get("1.0", "end-1c")

    try:
        valor_int_caixa1 = int(valor_caixa1)
        valor_int_caixa2 = int(valor_caixa2)

        print(f"Valor da Caixa 1 (int): {valor_int_caixa1}")
        print(f"Valor da Caixa 2 (int): {valor_int_caixa2}")
    except ValueError:
        tkinter.messagebox.showerror(title="Erro de valor",
                                     message="Erro ao processar quantidade de dias úteis. Digite uma valor valido")

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
            workbook.close()


opcoes = ["Reclassificação ", "Doc. Pessoais", "Nome da mãe", "Relatorio Hora Extra", "Relatorio de férias",
          "Deligamento de benefício", "Planilha de exceções"]

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



caret_up = ImageTk.PhotoImage(Image.open('./imagem/cima.png'))
caret_down = ImageTk.PhotoImage(Image.open('./imagem/baixo.png'))

menu_suspenso = tk.OptionMenu(window, var_opcao, *opcoes, command=opcao_selecionada)
menu_suspenso.configure(pady=20, padx=20, border=0, highlightthickness=1, font=('Arial', 16), indicatoron=0, image=caret_down, compound=tk.RIGHT, background="#E3E3E3", activebackground="#E3E3E3")
menu_suspenso.pack()
canvas.create_window(713.0, 481.0, window=menu_suspenso)

# Botoes

BotaoFinalizar = Button(
    image=ImagemBotaoFinalizar,
    borderwidth=0,
    highlightthickness=0,
    command=ValoresCaixa,
    relief="flat"
)

BotaoFinalizar.place(
    x=627.0,
    y=551.0,
    width=172.0,
    height=56.0
)

window.resizable(False, False)
window.mainloop()
