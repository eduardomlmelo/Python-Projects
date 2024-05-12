import tkinter as tk

def effect():
    open(https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/HelloWorld.svg/2560px-HelloWorld.svg.png)

window = tk.Tk()
window.title("Hello world")
label = tk.Label(window, text="Aperte o botão")
label.pack()

button = tk.Button(window, text="Aperte o botão", command=effect)
button.pack()

window.mainloop()