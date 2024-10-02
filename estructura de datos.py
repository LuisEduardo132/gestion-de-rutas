from tkinter import *
from PIL import Image, ImageTk

cabeza = Tk()
cabeza.title("Rutas De Transcaribe")
cabeza.config(bg="#e25e0c")
cabeza.geometry("500x600")

cabeza.resizable(False, False)

#Cargar imagen
imagen = Image.open("ts.png")

#Imagen RGBA para que sea transparente
imagen = imagen.convert("RGBA")

boton=Button(cabeza,text="BUSCAR", font=("Sans-Seriff",9), bg="#e25e0c", fg="white")
boton.place(x=350, y=200, anchor=CENTER)

Label(text="Busqueda:", font=("Sans-Seriff", 9, "bold"),fg="white", bg="#e25e0c").place(x=150, y=200, anchor=CENTER)

texto=Entry(cabeza)
texto.pack()
texto.place(x=250, y=200, anchor=CENTER)

#Redimensionar la imagen
imagen_redimensionada = imagen.resize((180, 130))

boton=Button(cabeza,text="REGISTRO DE RUTAS", font=("Sans-Seriff",14), bg="#e25e0c", fg="white")
boton.place(x=250, y=250, anchor=CENTER)

#Convertir la imagen redimensionada en un objeto que Tkinter pueda usar
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

#Etiqueta que contiene la imagen
label_imagen = Label(cabeza, image=imagen_tk, bg="#e25e0c")
label_imagen.place(x=170, y=5)

Label(text="RUTAS Y PARADAS DEL TRANSCARIBE", font=("Sans-Seriff", 18, "bold"),fg="white", bg="#e25e0c").place(relx=0.5, y=160, anchor=CENTER)

cabeza.mainloop()