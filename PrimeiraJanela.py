# Janela teste! NÃO USAR

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\54793421857\Desktop\Area\Primeira\Imagens")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("978x636")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 636,
    width = 978,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
ImagemBotaoIniciarPagina1 = PhotoImage(
    file=relative_to_assets("ImagemBotaoIniciarPagina1.png"))
Iniciar = Button(
    image=ImagemBotaoIniciarPagina1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
Iniciar.place(
    x=193.0,
    y=153.0,
    width=580.0,
    height=192.28729248046875
)

ImagemBotaoComoPagina1 = PhotoImage(
    file=relative_to_assets("ImagemBotaoComoPagina1.png"))
BotaoComoPagina1 = Button(
    image=ImagemBotaoComoPagina1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
BotaoComoPagina1.place(
    x=191.0,
    y=377.0,
    width=580.0,
    height=202.0714111328125
)

ImagemPagina1 = PhotoImage(
    file=relative_to_assets("ImagemPagina1.png"))
ImagemBGPagina1 = canvas.create_image(
    489.0,
    85.0,
    image=ImagemPagina1
)
window.resizable(False, False)
window.mainloop()
