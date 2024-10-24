import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup

# URL predefinida del manga y nombre del manga
URL_MANGA = "https://visortmo.com/library/manga/981/dandadan"
NOMBRE_MANGA = "Dandadan"
RUTA_IMAGEN = "Dandadan_fondo.jpeg"  # Reemplaza con la ruta de tu imagen


def obtener_ultimo_capitulo(url_manga):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url_manga, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        capitulo_enlace = soup.find('a', class_='btn-collapse')
        if capitulo_enlace:
            capitulo_texto = capitulo_enlace.text.strip()
            if "Capítulo" in capitulo_texto:
                try:
                    numero_capitulo = float(capitulo_texto.split('Capítulo')[-1].split()[0])
                    return numero_capitulo
                except ValueError:
                    return "Error al extraer el número del capítulo."
        return "No se encontró el enlace del capítulo."
    return f"Error al acceder a la página: {response.status_code}"

def mostrar_ultimo_capitulo():
    resultado = obtener_ultimo_capitulo(URL_MANGA)
    if isinstance(resultado, float):
        mensaje = f"El último capítulo de {NOMBRE_MANGA} es el capítulo {resultado}."
    else:
        mensaje = f"En {NOMBRE_MANGA}: {resultado}"
    messagebox.showinfo("Último Capítulo", mensaje)


def cargar_imagen():
    imagen = Image.open(RUTA_IMAGEN)
    imagen.thumbnail((300, 300))  # Ajusta el tamaño de la imagen según sea necesario
    tk_imagen = ImageTk.PhotoImage(imagen)
    label_imagen.config(image=tk_imagen)
    label_imagen.image = tk_imagen

# Configuración de la GUI
root = tk.Tk()
root.title(f"Verificador de Capítulos - {NOMBRE_MANGA}")

tk.Label(root, text=f"Verificador para: {NOMBRE_MANGA}").pack(pady=10)

tk.Button(root, text="Mostrar Último Capítulo", command=mostrar_ultimo_capitulo).pack(pady=10)

# Label para mostrar la imagen
label_imagen = tk.Label(root)
label_imagen.pack(pady=10)

# Cargar y mostrar la imagen
cargar_imagen()

root.mainloop()
