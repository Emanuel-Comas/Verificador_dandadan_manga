import requests
from bs4 import BeautifulSoup

def verificar_nuevo_capitulo(url_manga, capitulo_actual):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url_manga, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Buscar la etiqueta <a> con la clase "btn-collapse"
        capitulo_enlace = soup.find('a', class_='btn-collapse')
        
        if capitulo_enlace:
            # Extraer el texto que contiene el número de capítulo
            capitulo_texto = capitulo_enlace.text.strip()
            print(f"Texto del enlace: {capitulo_texto}")

            # Buscar el número en el texto
            # Se espera que el número esté después de la palabra 'Capítulo'
            if "Capítulo" in capitulo_texto:
                try:
                    # Extraer el número que aparece justo después de 'Capítulo'
                    numero_capitulo = float(capitulo_texto.split('Capítulo')[-1].split()[0])  # Toma el número después de 'Capítulo'
                    
                    if numero_capitulo > capitulo_actual:
                        print(f"¡Hay un nuevo capítulo! El último es el capítulo {numero_capitulo}")
                    else:
                        print(f"Aún no hay nuevo capítulo. El último sigue siendo el {capitulo_actual}.")
                except ValueError:
                    print(f"No se pudo extraer un número válido del texto: '{capitulo_texto}'")
            else:
                print("No se encontró la palabra 'Capítulo' en el texto del enlace.")
        else:
            print("No se pudo encontrar el enlace del capítulo.")
    else:
        print(f"Error al acceder a la página: {response.status_code}")

# URL del manga en Tumangaonline
url = "https://visortmo.com/library/manga/981/dandadan"
capitulo_actual = 166.00  # Ajusta esto al último capítulo que conoces

verificar_nuevo_capitulo(url, capitulo_actual)
