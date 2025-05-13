import tkinter as tk

def ativar_antivirus():
        



    janela = tk.Tk()
    janela.configure(bg="silver")
    janela.title("antivírus")
    janela.geometry("400x400")

    antivirus= tk.Label(janela,text="nosso sistema de antivírus já foi ativado", bg= "white", font=("Arial", 15))
    antivirus.pack(pady= 10)

    