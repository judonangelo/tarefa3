import tkinter as tk
import criararquivos
import ativarantivirus

def abrir_arquivo():
    criararquivos.criar_arquivo()


def abrir_antivirus():
    ativarantivirus.ativar_antivirus()






janela = tk.Tk()
janela.configure(bg='silver')
janela.title("janela")
janela.geometry("400x400")


cadastro = tk.Label(janela,text="cadastro", bg= "white", width=10, font=("Arial", 15))
cadastro.pack(pady= 5)

nome= tk.Label(janela,text="nome:", bg= "white", width=5, font=("Arial", 15))
nome.pack(pady= 3)

caixadetexto1 = tk.Entry(janela, bg="white")
caixadetexto1.pack(pady=10)


nome= tk.Label(janela,text="senha:", bg= "white", width=5, font=("Arial", 15))
nome.pack(pady= 3)

caixadetexto2 = tk.Entry(janela, bg="white")
caixadetexto2.pack(pady=10)


btn_enter =  tk.Button(janela, text= "enter",font = ("Arial", 10), command=abrir_arquivo)
btn_enter.pack(pady=10)



btn_recuperar =  tk.Button(janela, text= "recuperar senha",font = ("Arial", 10))
btn_recuperar.pack(pady=10)


btn_antivirus = tk.Button(janela, text = "ativar antivírus", font = ("Arial", 10), command=abrir_antivirus)
btn_antivirus.pack( pady = 10)




janela.mainloop()