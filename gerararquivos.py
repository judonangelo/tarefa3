import tkinter as tk

def gerar_arquivos():
        

    janela = tk.Tk()
    janela.configure(bg="silver")
    janela.title("gerar arquivo")
    janela.geometry("400x400")


    gerararquivos = tk.Label(janela, text= "um arquivo foi criado", bg= "white", font=("Arial", 15))
    gerararquivos.pack(pady= 10)
