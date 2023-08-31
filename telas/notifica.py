from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk, Canvas, Button, PhotoImage
import json
is_popup_open = False

def aviso(aviso):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame0"

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    if aviso == "success":
        imagem = "sucesso.png"
    elif aviso == "aguarde":
        imagem = "aguarde.png"
    else:
        imagem = "erro.png"

    popup = tk.Toplevel()
    popup.grab_set()
    popup.title("Aviso!")
    popup.geometry("750x240")
    popup.configure(bg = "#110E0E")
    window_width = 750
    window_height = 240
    position_top = int(popup.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    popup.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    close_image = tk.PhotoImage(file=relative_to_assets(imagem)) 
    close_button = tk.Button(popup, image=close_image, command=popup.destroy)
    close_button.image = close_image  # Mantém uma referência à imagem para evitar que ela seja coletada como lixo
    close_button.place(x=window_width/2, y=window_height/2, anchor="center")

    return popup  # Retornamos o objeto Toplevel para que possamos verificar seu estado mais tarde

def set_popup_open(state):
    global is_popup_open
    is_popup_open = state
    print(is_popup_open)
    
def configure_data(data):
    popup = tk.Toplevel()
    popup.title("Pop-up Window")
    popup.geometry("300x200")
    window_width = 500
    window_height = 500
    position_top = int(popup.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(popup.winfo_screenwidth() / 2 - window_width / 2)
    popup.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
   
    label1 = tk.Label(popup, text="Email Remetente:")
    label1.pack()

    text1 = tk.StringVar()  # Cria uma variável do Tkinter
    text1.set(data["emailSender"])
    entry1 = tk.Entry(popup, textvariable=text1)  # Vincula a variável ao campo de entrada
    entry1.pack()

    label2 = tk.Label(popup, text="Email Destinatário:")
    label2.pack()

    text2 = tk.StringVar()  # Cria uma variável do Tkinter
    text2.set(data["emailRecipient"])
    entry2 = tk.Entry(popup, textvariable=text2)  # Vincula a variável ao campo de entrada
    entry2.pack()

    def close_popup():
        print("Texto 1:", text1.get())  # Obtém o valor da variável
        print("Texto 2:", text2.get())  # Obtém o valor da variável
        data = {"emailSender":text1.get(), "emailRecipient":text2.get()}
        escreveJson(data)
        popup.destroy()

    close_button = tk.Button(popup, text="Close", command=close_popup)
    close_button.pack()
def escreveJson(data):
    with open('assets/dados.json', 'w') as f:
        json.dump(data, f)
