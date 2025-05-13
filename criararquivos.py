import tkinter as tk
import gerararquivos
import escrevertexto

def abrirtexto():
    escrevertexto.escrever()


def abrir_arquivo2():
    gerararquivos.gerar_arquivos()


def criar_arquivo():
        

    janela = tk.Tk()
    janela.configure(bg='silver')
    janela.title("arquivos")
    janela.geometry("400x400")

    arquivos = tk.Label(janela,text="arquivos", bg= "white", width=10, font=("Arial", 15))
    arquivos.pack(pady= 5)



    btn_criar =  tk.Button(janela, text= "criar arquivo",font = ("Arial", 10), command=abrir_arquivo2)
    btn_criar.pack(pady=10)


    editor = tk.Label(janela,text="editor de texto/bloco de notas", bg= "white", font=("Arial", 15))
    editor.pack(pady= 5)

    btn_abrir =  tk.Button(janela, text= "abrir editor de texto",font = ("Arial", 10), command = abrirtexto)
    btn_abrir.pack(pady=10)

    






    