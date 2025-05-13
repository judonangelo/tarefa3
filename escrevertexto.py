import tkinter as tk



def escrever():
        


    janela = tk.Tk()
    janela.configure(bg="silver")
    janela.title("escrever texto")
    janela.geometry("400x400")


    def confirmar():
        janela.destroy()


    escrevertexto = tk.Entry(janela, bg= "white", font=("Arial", 15))
    escrevertexto.pack(pady= 10)



    btn_confirmar = tk.Button(janela, bg="white", text = "confirmar", font=("Arial", 15), command = confirmar)
    btn_confirmar.pack(pady= 10)
