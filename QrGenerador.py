from cgitb import text
import qrcode  # pip install qrcode
import os
import tkinter as tk
import time


def generarQR(texto):
    qrcode.make(texto).save("QR.png")
    print("QR generado con exito")

    # os.system("QR.png")
    # print("QR mostrado con exito")
# text = input("Ingrese el texto a codificar: ")
text = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
generarQR(text)
window = tk.Tk()
window.title("QR")
window.geometry('400x800')
img = tk.PhotoImage(file="QR.png")

tk.Label(window, image=img).pack()

tk.Text(window,
        height=4,
        width=10).pack()
tk.Label(window, text=text).pack()

tk.Button(window, text="Cerrar", command=window.destroy).pack()
window.mainloop()
time.sleep(2)
os.remove("QR.png")
