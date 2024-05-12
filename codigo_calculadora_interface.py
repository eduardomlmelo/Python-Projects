import tkinter as tk

def atualizar_tela(valor):
    expressao = tela.get()
    tela.delete(0, tk.END)
    tela.insert(0, expressao + valor)

def calcular():
    expressao = tela.get()
    try:
        resultado = eval(expressao)
        tela.delete(0, tk.END)
        tela.insert(0, str(resultado))
    except:
        tela.delete(0, tk.END)
        tela.insert(0, "Erro")

janela = tk.Tk()
janela.title("Calculadora")

tela = tk.Entry(janela)
tela.grid(row=0, column=0, columnspan=4)

botoes = [
    "9","8","7","/",
    "6","5","4","*",
    "3","2","1","-",
    "0",".","=","+"
]
row, col = 1,0

for botao in botoes:
    if botao == "=":
        tk.Button(janela, text=botao, padx=20, pady=20, command=calcular).grid(row=row, column=col)
    else:
        tk.Button(janela, text=botao, padx=20, pady=20, command=lambda v=botao: atualizar_tela(v)).grid(row=row, column=col)
    col+=1
    if col > 3:
        col = 0
        row+=1
janela.mainloop()