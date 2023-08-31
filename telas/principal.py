
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
from models.controller import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

def telaInicial():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets/frame0"


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("1440x700")
    window.configure(bg = "#1A1919")

    window_width = 1440
    window_height = 700
    position_top = int(window.winfo_screenheight() / 2 - window_height / 2)
    position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
    window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        
    canvas = Canvas(
        window,
        bg = "#1A1919",
        height = 700,
        width = 1440,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        1440.0,
        106.0,
        fill="#F2F2F2",
        outline="")

    canvas.create_text(
        35.0,
        34.0,
        anchor="nw",
        text="ScriptPulse",
        fill="#000000",
        font=("Inter Bold", 32 * -1)
    )
    btn_config = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=btn_config,
        borderwidth=0,
        highlightthickness=0,
        command=btn_configure,
        relief="raised"
    )
    button_2.place(
        x=1211.0,
        y=0.0,
        width=229.0,
        height=106.0
    )

    btn_files = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=btn_files,
        borderwidth=0,
        highlightthickness=0,
        command=btn_select_file,
        relief="flat"
    )
    button_3.place(
        x=565.0,
        y=162.0,
        width=311.0,
        height=305.0
    )
    window.resizable(False, False)
    window.mainloop()
