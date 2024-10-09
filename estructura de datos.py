from tkinter import *
from PIL import Image, ImageTk
from rutas import rutas_transcaribe, obtener_info_ruta  # Asegúrate de tener estos importados

cabeza = Tk()
cabeza.title("Rutas De Transcaribe")
cabeza.config(bg="#e25e0c")
cabeza.geometry("500x600")
cabeza.resizable(False, False)

# Cargar imagen
imagen = Image.open("ts.png")
imagen = imagen.convert("RGBA")  # Para que sea transparente
imagen_redimensionada = imagen.resize((180, 130))  # Redimensionar la imagen
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

# Etiqueta que contiene la imagen
label_imagen = Label(cabeza, image=imagen_tk, bg="#e25e0c")
label_imagen.place(x=170, y=5)

# Etiqueta principal
Label(text="RUTAS Y PARADAS DEL TRANSCARIBE", font=("Sans-Seriff", 18, "bold"), fg="white", bg="#e25e0c").place(relx=0.5, y=160, anchor=CENTER)

# Campo de búsqueda
Label(text="Busqueda:", font=("Sans-Seriff", 9, "bold"), fg="white", bg="#e25e0c").place(x=150, y=190, anchor=CENTER)

# Crear el campo de texto
texto = Entry(cabeza)
texto.place(x=250, y=190, anchor=CENTER)

# Función para convertir el texto del Entry a mayúsculas automáticamente
def convertir_a_mayusculas(*args):
    texto_str.set(texto_str.get().upper())  # Convierte el texto a mayúsculas

# Variable que almacena el texto del Entry
texto_str = StringVar()
texto_str.trace("w", convertir_a_mayusculas)  # Activa la función cuando se modifica el texto

# Configurar el campo de texto para usar la variable
texto.config(textvariable=texto_str)

# Frame para contener el scrollbar y el Text
frame = Frame(cabeza)
frame.place(x=50, y=250, width=400, height=300)

# Widget Text para mostrar resultados (se deshabilitará la edición)
label_resultados = Text(frame, wrap=WORD, bg="#e25e0c", fg="white", font=("Sans-Seriff", 9), state=DISABLED)
label_resultados.pack(side=LEFT, fill=BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(frame, command=label_resultados.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configurar el Text para que use el scrollbar
label_resultados.config(yscrollcommand=scrollbar.set)

# Función para mostrar todas las rutas
def mostrar_rutas():
    resultado = "Rutas Disponibles:\n\n"  # Título de la sección
    for ruta, detalles in rutas_transcaribe.items():
        resultado += f"Ruta: {ruta}\n"
        resultado += f"  Horarios:\n"
        resultado += f"    - Lunes a Viernes: {detalles['horarios']['lunes_viernes']}\n"
        resultado += f"    - Sábados: {detalles['horarios'].get('sabados', 'No disponible')}\n"
        resultado += f"    - Domingos: {detalles['horarios'].get('domingos', 'No disponible')}\n"
        resultado += f"  Estaciones: {', '.join(detalles['estaciones'])}\n"
        resultado += "----------------------------------\n"  # Separador entre rutas

    label_resultados.config(state=NORMAL)  # Habilitar el Text para modificar su contenido
    label_resultados.delete(1.0, END)  # Limpiar el Text antes de mostrar nuevos resultados
    label_resultados.insert(END, resultado)  # Insertar resultados en el Text
    label_resultados.config(state=DISABLED)  # Deshabilitar el Text para que no se pueda editar

# Función para buscar una ruta específica
def buscar_ruta():
    ruta = texto.get().strip()  # Obtener texto del campo de búsqueda
    resultado = obtener_info_ruta(ruta)
    label_resultados.config(state=NORMAL)  # Habilitar el Text para modificar su contenido
    label_resultados.delete(1.0, END)  # Limpiar el Text antes de mostrar nuevos resultados
    label_resultados.insert(END, resultado)  # Insertar resultado en el Text
    label_resultados.config(state=DISABLED)  # Deshabilitar el Text para que no se pueda editar

# Botón para buscar rutas
boton_buscar = Button(cabeza, text="BUSCAR", font=("Sans-Seriff", 9), bg="#e25e0c", fg="white", command=buscar_ruta)
boton_buscar.place(x=350, y=190, anchor=CENTER)

# Botón para mostrar todas las rutas
boton_registro = Button(cabeza, text="REGISTRO DE RUTAS", font=("Sans-Seriff", 14), bg="#e25e0c", fg="white", command=mostrar_rutas)
boton_registro.place(x=250, y=225, anchor=CENTER)

cabeza.mainloop()