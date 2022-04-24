import qrcode  # pip install qrcode
import os
import tkinter as tk
import time

#Crear ventanas de tkinter
window = tk.Tk()
window.title("QR")
window.geometry('800x800')

# valores vacios
img = tk.PhotoImage(file="")
text = ""
#definir el texto que se va a mostrar en el QR
def generarQR(texto):
    qrcode.make(texto).save("QR.png")
    print("QR generado con exito")
    
def valorQR():
    texto = entry.get()

def valorQR():
    texto = entry.get()
    generarQR(texto)
    img = tk.PhotoImage(file="QR.png")
    imageLabel.configure(image=img)
    imageLabel.image = img
    
#funcion para agrupar funciones y ejecutarlas e un solo comando
def all_functions():
    print(entry.get()), 
    valorQR()

img = tk.PhotoImage(file="")
text = ""
generarQR(text)

frame = tk.Frame(height=500, width=500)

imageLabel = tk.Label(window, image=img)

entry = tk.Entry(window, width=50)

texto = tk.Label(window, textvariable=text)

Generate = tk.Button(window, text="Generar QR", command=all_functions)
# tk.Button(window, text="Generar QR", command=lambda: [print(entry.get()), window.update(),valorQR]).pack()

showQR =tk.Button(window, text="Mostrar QR", command=lambda: os.system("QR.png"))

close = tk.Button(window, text="Cerrar", command=window.destroy, height=5)

imageLabel.pack()
entry.pack()
texto.pack()
Generate.pack()
showQR.pack()
close.pack()
window.mainloop()

time.sleep(2)
os.remove("QR.png")
